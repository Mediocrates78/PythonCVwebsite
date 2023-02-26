let container = document.querySelector(".sud_wrapper")

buildGrid()

function buildGrid() {
    
    for (let x = 0; x < 9; x++) {
        for (let y = 0; y < 9; y++) {
            if (unsolved[x][y] == 0) {
                unsolved[x][y] = ""
            }
            let plotId = x.toString() + y.toString()
            const plot = document.createElement('input')
            plot.setAttribute('class', 'sud_plot')
            plot.setAttribute('value', unsolved[x][y])
            plot.setAttribute('id', plotId)
            plot.setAttribute('maxlength', 1)
            plot.addEventListener('keyup', numFilter)
            plot.style.gridColumn = x + 1
            plot.style.gridRow = y + 1
            container.append(plot)
        }
    }
}

function numFilter() {
    let entered = this.value
    const nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    if (nums.includes(entered)) {
        pass
    } else {
        this.value = ""
    }
}

const btn = document.getElementById("solve");
btn.addEventListener('click', function onClick() {
    for (let x = 0; x < 9; x++) {
        for (let y = 0; y < 9; y++) {
            const plotId = x.toString() + y.toString()
            let plot = document.getElementById(plotId)
            plot.setAttribute('value', solved[x][y])
        }
    }
})



