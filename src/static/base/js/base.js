document.addEventListener('DOMContentLoaded', () => {
    init()
})

const init = () => {
    document.querySelectorAll('.js-base__stop-click-propagation').forEach(element => {
        element.addEventListener('click', stopPropagation)
    })
}

/**
 * クリックイベントの伝搬を止める。
 *
 * @param {Event} event クリックイベント
 */
const stopPropagation = (event) => {
    event.stopPropagation()
}
