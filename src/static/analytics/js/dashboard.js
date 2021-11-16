document.addEventListener('DOMContentLoaded', () => {
    initGraph()
    initMetricsList()
})

/**
 * グラフの描画を初期化する。
 */
const initGraph = () => {
    fetch(`/metrics_data/?${buildParams()}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`${res.status}: ${res.statusText}`)
        }
        return response.json()
    })
    .then(response => {
        Plotly.react(
            document.querySelector('.js-dashboard__graph'),
            response,
        )
    })
    .catch((reason) => {
        console.log(reason)
    })
}

/**
 * メトリクス一覧のチェックボックスを初期化する。
 */
const initMetricsList = () => {
    const metricsRowNodeList = document.querySelectorAll('.js-dashboard__metrics-row')
    metricsRowNodeList.forEach(metricsRowNode => {
        metricsRowNode.addEventListener('click', selectMetricsRow)
    })
}

/**
 * メトリクス一覧チェックボックスのクリック時処理。
 *
 * @param {Event} event クリックイベント
 */
const selectMetricsRow = (event) => {
    const checkbox = event.currentTarget.querySelector('input')
    checkbox.checked = !checkbox.checked
    initGraph()
}

/**
 * メトリクス取得用クエリ文字列を生成する。
 *
 * @returns {string} クエリ文字列
 */
const buildParams = () => {
    const metricsRowNodeList = document.querySelectorAll('.js-dashboard__metrics-row')
    let query = []
    metricsRowNodeList.forEach(metricsRowNode => {
        const input = metricsRowNode.querySelector('input')
        if (input.checked) {
            query.push(`metrics_id=${input.value}`)
        }
    })
    return query.join('&')
}
