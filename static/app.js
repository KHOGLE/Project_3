//The github that has api calling https://git.bootcampcontent.com/Michigan-State-University/MSU-VIRT-DATA-PT-03-2023-U-LOLC/-/blob/main/Class/15-Mapping/2/Activities/03-Stu_MarkerClusters/Solved/static/js/logic.js
// const fullDataURL = "http://127.0.0.1:5000/api/v1.0/full_data.json"

function initialize(){
d3.json("Resources/Project3.LABusinesses.json").then((data) => {
    console.log(data)
});
}
initialize();
// function innt(){
//     d3.json(fullDataURL).then(function(data){
//         console.log(data)
// //         // let Districts = data;
// //         // let dropDown = d3.select("#selDataset");
//     })
// };

//     for (let xx of x){
//         dropDown.append("option").attr('value', id).text(id);
//        }
    
//     optionChanged(xCall);
    
// }

// function optionChanged(x){
//     // some sort of call
//         info(x, data);
//         graph1(x, data);
//         graph2(x,data);
//         graph3(x,data);
// }

// function info(Districts){
    //

// }

// function graph1(x,data){
 
    // let graphdata = []
    // let layout = {}
    // Plotly.newPlot("graph1", graphdata, layout);
// }

// function graph2(x,data){
    
    
    
//     let graphdata = []
//     let layout = {}
//     Plotly.newPlot("graph2", graphdata, layout);
// }

// function graph3(x,data){
    


//     let graphdata = []
//     let layout = {}
//     Plotly.newPlot("graph3", graphdata, layout);
// }

// innt();