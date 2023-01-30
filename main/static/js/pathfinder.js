let gridDisplay = document.querySelector('#grid')
gridDisplay.style.display = 'grid'
gridDisplay.style.width = '600px'
gridDisplay.style.height = '600px'

buildGrid()
let startEnd = 0
let coords = []

function buildGrid() {
    for (let x = 0; x < 20; x ++) {
        for (let y = 0; y < 20; y++) {
            const plot = document.createElement('button')
            let xStr = ('0' + x.toString()).slice(-2)
            let yStr = ('0' + y.toString()).slice(-2)
            let plotId = xStr + yStr
            plot.setAttribute('class', 'path_button')
            plot.setAttribute('id', plotId)
            plot.style.backgroundColor = 'white'
            plot.style.color = "black"
            plot.addEventListener('click', clicked)
            plot.style.gridColumn = x + 1
            plot.style.gridRow = y + 1
            gridDisplay.append(plot)
        }

    }
}

function clicked() {
    let plotColor = this.style.backgroundColor
    let plotIdNumber = this.id
    const clickedPlot = this

    if (startEnd == 0) {
        clickedPlot.style.backgroundColor = "red"
        coords.push(clickedPlot.id)
        startEnd ++
    } else {
        clickedPlot.style.backgroundColor = "blue"
        coords.push(clickedPlot.id)
        const steps = getSteps()
        markSteps(steps)
    }
}

function getSteps() {
    let colSteps = [], rowSteps = [], steps = []
    let cols = [parseInt(coords[0].slice(0, 2)), parseInt(coords[1].slice(0, 2))].sort((a, b)=>a-b)
    let rows = [parseInt(coords[0].slice(2)), parseInt(coords[1].slice(2))].sort((a, b)=>a-b)
    for (let i = cols[0]; i < cols[1] + 1; i++) {colSteps.push(i)}
    for (let i = rows[0]; i < rows[1] + 1; i++) {rowSteps.push(i)}
    if (colSteps.length > rowSteps.length) {
        while (colSteps.length > rowSteps.length) {rowSteps = rowSteps.concat(rowSteps)}
        rowSteps = rowSteps.slice(0, colSteps.length).sort((a, b)=>a-b)
    } else if (rowSteps.length > colSteps.length){
        while (rowSteps.length > colSteps.length) {colSteps = colSteps.concat(colSteps)}
        colSteps = colSteps.slice(0, rowSteps.length).sort((a, b)=>a-b)
    } else {}
    if (parseInt(coords[0].slice(0, 2)) > parseInt(coords[1].slice(0, 2))){
        colSteps = colSteps.sort((a, b)=>b-a)
    }
    if (parseInt(coords[0].slice(2)) > parseInt(coords[1].slice(2))){
        rowSteps = rowSteps.sort((a, b)=>b-a)
    }
    return steps = colSteps.map(function(x, y) {return [x, rowSteps[y]]})
}

function markSteps(steps) {
    for (let x in steps) {
        let coord = ("0" + steps[x][0].toString()).slice(-2) + ("0" + steps[x][1].toString()).slice(-2)
        const mark = document.getElementById(coord)
        mark.append(x)
    }
}
