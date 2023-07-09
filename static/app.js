

function innt(){
    // some sort of calling
    let x = ;
    let dropDown = d3.select("#selDataset");

    for (let xx of x){
        dropDown.append("option").attr('value', id).text(id);
       }
    
    optionChanged(xCall);
    
}

function optionChanged(x){
    // some sort of call
        info(x, data);
        graph1(x, data);
        graph2(x,data);
        graph3(x,data);
}

function info(x, data){

}

function graph1(x,data){
    
    
    
    let graphdata = []
    let layout = {}
    Plotly.newPlot("graph1", graphdata, layout);
}

function graph2(x,data){
    
    
    
    let graphdata = []
    let layout = {}
    Plotly.newPlot("graph2", graphdata, layout);
}

function graph3(x,data){
    


    let graphdata = []
    let layout = {}
    Plotly.newPlot("graph3", graphdata, layout);
}

innt();