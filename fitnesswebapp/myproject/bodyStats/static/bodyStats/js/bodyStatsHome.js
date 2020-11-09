/**
 *
 * @function updateUserBodyStats()
 * This function get the data that the user has entered into the update body stats forms in bodyStatsHome.html.
 * To test that the js has gotten the correct values in the correct format, the users input is outputted to the console.
 * If the user has selected to to input their body stats
 *
 */

function updateUserBodyStats() {

    let bodyWeight = document.getElementById('updateBodyStats').elements.namedItem("bodyStatWeight").value;
    const bodyWeightUnit = document.getElementById('updateBodyStats').elements.namedItem("unitWeight").value;
    let bodyHeight = document.getElementById('updateBodyStats').elements.namedItem("bodyStatHeight").value;
    const bodyHeightUnit = document.getElementById('updateBodyStats').elements.namedItem("unitHeight").value;
    const bodyStatsDate = document.getElementById('updateBodyStats').elements.namedItem("bodyStatDate").value;

    // console.log("Weight: " + bodyWeight + " " + bodyHeightUnit + "\nHeight: " + bodyHeight + " " + bodyWeightUnit + "\nDate: " + bodyStatsDate);

    if (bodyWeightUnit === "lb") {
        const bodyWeightTemp = (bodyWeight * 2.205);
        bodyWeight = bodyWeightTemp.toFixed(2);
    }

    if (bodyHeightUnit === "inches") {
        const bodyHeightTemp = (bodyHeight * 2.54);
        bodyHeight = bodyHeightTemp.toFixed(2);
    }

    if (bodyHeight <= 135 || bodyHeight >= 200 ) {
        alert("Please enter in a valid height");
    }

    if (bodyWeight <= 35 || bodyWeight >= 200) {
        alert("Please enter in a valid weight");
    }

    const bodyStatsBMI = calculateBMI(bodyHeight, bodyWeight);
    //console.log(bodyStatsBMI);

    let updatedBodyStats = {
        "weight": bodyWeight,
        "height": bodyHeight,
        "date": bodyStatsDate,
        "BMI": bodyStatsBMI
    };

    let updatedBodyStatsJSON = JSON.stringify(updatedBodyStats);

    console.log(updatedBodyStats);
    console.log(updatedBodyStatsJSON);

}

/**
 *
 * @function calculateBMI()
 * This functions takes in the user height and weight as parameters. It then converts the users height from centimeters
 * to meters by dividing the users height by 100. It then calculates the users BMI by dividing the users body weight
 * by their height squared, and then round to two decimals places.
 *
 * @param bodyHeight - the height of the user in centimeters
 * @param bodyWeight - the weight of the user in kilograms
 *
 * @return {number} BMI - the BMI of the user
 *
 */

function calculateBMI(bodyHeight, bodyWeight) {
    //console.log(bodyHeight);
    //console.log(bodyWeight);
    const heightMeters = (bodyHeight / 100);
    const BMI = (bodyWeight / (heightMeters * heightMeters)).toFixed(2);
    //console.log("Height: " + bodyHeight + "\nWeight: " + bodyWeight + "\nBMI: " + BMI);
    return BMI;
}

