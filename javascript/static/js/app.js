function answer(ans){
    var PANEL = d3.select("#answer");
    PANEL.html("");
    PANEL.append("h6").text('Answer ' + ans);
    console.log("answer: " + ans)
}

function dummy(){
    alert("This is messed up");
}
var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "",
  password: ""
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
});
//d3.select('#yes-btn').on('click', dummy);
//d3.select('#no-btn').on('click', answer("no")); 
//d3.selectAll('button').on('click', console.log('answer'));
