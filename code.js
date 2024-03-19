document.addEventListener("DOMContentLoaded", function () {

    let arr = [];
    arr.push(`images/comp_cloud.png`);
    arr.push(`images/comp_tifa.png`);
    arr.push(`images/comp_barret.png`);
    arr.push(`images/comp_aerith.png`);
    arr.push(`images/comp_armor.png`);
 


    document.getElementById("cloud").addEventListener("click", function() {
        graph.src = arr[0];
    });

    document.getElementById("tifa").addEventListener("click", function() {
        graph.src = arr[1];
    });

    document.getElementById("barret").addEventListener("click", function() {
        graph.src = arr[2];
    });

    document.getElementById("aerith").addEventListener("click", function() {
        graph.src = arr[3];
    });

    document.getElementById("armor").addEventListener("click", function() {
        graph.src = arr[4];
    });



});