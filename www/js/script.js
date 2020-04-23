//load header(nav) and footer
$(document).ready(function () {
  $('.nav-placeholder').load('/html/nav.html', function () {
    $('.navbar .nav-item').each(function () {
      if ($(this).find('.nav-link').attr('href') === window.location.pathname) {
        $(this).addClass('active')
      }
    })
  })
  $('.footer-placeholder').html(`<footer class="text-muted">
    <div class="container">
        <p>Hello World 2020!</p>
    </div></footer>`)
})


/**
 * log related
 */

/**
 * @param {string} logName log's name without directory path
 * @param {int} num recent log numbers to download
 */
function downloadAndShowLog(logName, num) {
  let logs = []
  $.get('/getRecentLog', {'name': logName, 'num': num || ''}, function (result) {
    if (result === '')
      logs = [`There is no log in ${logName}.`]
    else
      logs = result.trimEnd().split(/[\n\r]+/)
    $('#totalLogCount').text(logs.length)
    let perPage = 30,
      totalPages = Math.ceil(logs.length / perPage)
    showLogsAtPage(logs, -1, perPage)
    createPagination(totalPages, -1, (index) => showLogsAtPage(logs, index, perPage), 10)
  })
}

/**
 * Generate pagination with additional two nav button, looks like nav_left/n/.../m/m+1/.../1/nav_right
 * Pagination is in reversed order, the left page number is larger.
 * @param {int} pageCount total page count.
 * @param {int} curPage 0<=curPage<totalPages, shown text is curPage+1.
 * @param {function} callback called when click, active page or disabled nav button will ignore the callback
 * @param {int} shownNum shown pagination button number,
 **/
function createPagination(pageCount, curPage = -1, callback, shownNum = 10) {
  // TODO: add 'reversed'
  // validation for params
  if (pageCount < shownNum) {
    shownNum = pageCount
  }
  curPage = (curPage < 0 || curPage >= pageCount) ? pageCount - 1 : curPage; //default the newest page
  // decide which pages to show
  let shownPages = [curPage];
  for (let i = 1; i < shownNum; i++) {
    if (curPage + i < pageCount && shownPages.length < shownNum)
      shownPages.unshift(curPage + i)
    if (curPage - i >= 0 && shownPages.length < shownNum) {
      shownPages.push(curPage - i)
    }
  }
  // always keep the first and last page
  shownPages[0] = pageCount - 1;
  shownPages[shownNum - 1] = 0;

  // ready to render html
  let $pagination = $('.pagination');
  if ($pagination.first().children().length !== shownNum + 2) {
    // pagination buttons only created once
    $pagination.html([
      '<li class="page-item unselectable"><a class="page-link" aria-label="Later"><span>&nbsp;&laquo;&nbsp;</span></a></li>',
      '<li class="page-item unselectable"><a class="page-link"></a></li>\n'.repeat(shownNum),
      '<li class="page-item unselectable"><a class="page-link" aria-label="Earlier"><span>&nbsp;&raquo;&nbsp;</span></a></li>'
    ].join('\n'))
  }

  // Then to update page numbers and bind click event
  let _onclick = function (index) {
    if ($.isFunction(callback))
      callback(index)
    createPagination(pageCount, index, callback, shownNum)
  }
  $pagination.each(function () {
    $(this).find('.page-item').each(function (index) {
      let $button = $(this), $link = $button.find('a')
      $button.removeClass('disabled').removeClass('active')
      $link.unbind('click')
      if (index === 0) {//  left
        if (curPage === pageCount - 1) {
          $button.addClass('disabled')
        } else {
          $link.click(() => _onclick(curPage + 1))
        }
      } else if (index === shownNum + 1) {//right
        if (curPage === 0) {
          $button.addClass('disabled')
        } else {
          $link.click(() => _onclick(curPage - 1))
        }
      } else {
        //left, t-1, t-2, ~ , 1, 0, right
        let pageNo = shownPages[index - 1]
        if (curPage === pageNo) {
          $button.addClass('active')
        } else {
          $link.click(() => _onclick(pageNo))
        }
        // set page text: index+1 or "..."
        if ((index === 2 && Math.abs(shownPages[0] - shownPages[1]) !== 1)
          || (index === shownNum - 1 && Math.abs(shownPages[shownNum - 1] - shownPages[shownNum - 2]) !== 1)) {
          $link.text('...')
        } else {
          $link.text((pageNo + 1).toString())
        }
      }
    })
  })
}

/**
 * Show index-th page of logs.
 * @param {string[]} data log data, already divided to string list.
 * @param {int} index default(or invalid value) the latest page
 * @param {int} perPage shown log number per page
 */
function showLogsAtPage(data, index, perPage) {
  let totalPages = Math.ceil(data.length / perPage)
  index = index < 0 || index >= totalPages ? totalPages - 1 : index
  let startNo = -(totalPages - index) * perPage,
    endNo = startNo + perPage
  let shownLogs = data.slice(Math.max(startNo, -data.length), endNo === 0 ? undefined : endNo)
  console.log(`show ${shownLogs.length} logs at page ${index}`)
  let $panel = $('pre.codes'),
    $codes = $panel.find('code')
  if ($codes.length !== perPage) {
    $panel
      .html(shownLogs.map((e) => `<code>${$('<div/>').text(e).html()}</code>`).join('\n'))
    // .css('counter-reset', `step ${startNo}`)
  } else {
    $codes.each(function (index) {
      let $code = $(this)
      if (index < shownLogs.length)
        $code.text(shownLogs[index]).show()
      else
        $code.hide()
    })
  }
}


/**
 * show directory folder/file structure
 * @param {string} path key in window.dirTreeData, same as relative filepath on server
 */
function jumpToDirectory(path) {
  window.location.hash = '#' + path
  let folders = path.split(/[/\\]+/)
  let items = []
  for (let i = 0; i < folders.length - 1; i++) {
    let nodePath = folders.slice(0, i + 1).join('\\')
    items.push(`<li class="breadcrumb-item"><a data-path="${nodePath}" href="#${nodePath}">${folders[i]}</a></li>`)
  }
  items.push(`<li class="breadcrumb-item active" aria-current="page">${folders[folders.length - 1]}</li>`)
  $('.breadcrumb').html(items.join('')).find('a').click(function () {
    jumpToDirectory($(this).data('path'))
  })
  let treeNodes = []
  $.each(window.dirTreeData[path]['folders'], function (index, value) {
    treeNodes.push(`<a data-path="${path + '\\' + value}" class="list-group-item list-group-item-action">
        <svg class="bi bi-folder" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
          <path d="M9.828 4a3 3 0 01-2.12-.879l-.83-.828A1 1 0 006.173 2H2.5a1 1 0 00-1 .981L1.546 4h-1L.5 3a2 2 0 012-2h3.672a2 2 0 011.414.586l.828.828A2 2 0 009.828 3v1z"/>
          <path fill-rule="evenodd" d="M13.81 4H2.19a1 1 0 00-.996 1.09l.637 7a1 1 0 00.995.91h10.348a1 1 0 00.995-.91l.637-7A1 1 0 0013.81 4zM2.19 3A2 2 0 00.198 5.181l.637 7A2 2 0 002.826 14h10.348a2 2 0 001.991-1.819l.637-7A2 2 0 0013.81 3H2.19z" clip-rule="evenodd"/>
        </svg> ${value}</a>`)
  })
  $.each(window.dirTreeData[path]['files'], function (index, value) {
    treeNodes.push(
      `<button data-path="${path + '\\' + value}" type="button" class="list-group-item list-group-item-action"
            data-toggle="modal" data-target="#imageModal">${value}</button>`)
  })
  $('#dirTree').html(treeNodes.join(''))
  $('#dirTree a').click(function () {
    jumpToDirectory($(this).data('path'))
  })
  $('#dirTree button').click(function () {
    let imgPath = $(this).data('path')
    $('#imageModalLabel').text($(this).text())
    $('#imageModal .modal-body img').attr('src', '/getImage?path=' + imgPath)
  })
}