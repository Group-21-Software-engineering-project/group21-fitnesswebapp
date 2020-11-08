function validateBodyStats () {
    var bodyWeight = document.getElementById("bodyStatWeight").value;
    var bodyWeightUnit = document.getElementById("unitWeight").value;
    var bodyHeight = document.getElementById("bodyStatHeight").value;
    var bodyHeightUnit = document.getElementById("unitHeight").value;
    var bodyStatsDate = document.getElementById("bodyStatDate").value;

    console.log("Weight: " + bodyWeight + " " + bodyHeightUnit);
    console.log("Height: " + bodyHeight + " " + bodyWeightUnit);
    console.log("Date: " + bodyStatsDate);

    if (bodyWeightUnit === "lb") {
        var bodyWeightTemp = (bodyWeight * 2.205);
        bodyWeight = bodyWeightTemp.toFixed(2);
    }

    if (bodyHeightUnit === "inches") {
        var bodyHeightTemp = (bodyHeight * 2.54);
        bodyHeight = bodyHeightTemp.toFixed(2);
    }

    if (bodyHeight <= 135 || bodyHeight >= 200 ) {
        alert("Please enter in a valid height");
    }

    if (bodyWeight <= 35 || bodyWeight >= 200) {
        alert("Please enter in a valid weight");
    }


}