/**
 *
 * @function updateUserBodyStats()
 * This function gets the data that the user has entered into the update body stats forms in bodyStatsHome.html.
 * To test that the js has gotten the correct values in the correct format, the users input is outputted to the console.
 * The users height and weigh is validated to ensure that the value that the user has inputted is with a set range, to
 * prevent problems from occurring if the users input negative values. If the user has selected to input their body
 * stats in imperial, the function will convert their stats into metric and then rounds the users body stats to two
 * decimal places. The function then calls upon the function calculateBMI() passing in values of the users height
 * and weight. All of the users stats are then placed into an object updatedBodyStats. The object is then turned into
 * a JSON object so it can then be sent to the back end of the website.
 *
 */

function updateUserBodyStats() {

    let bodyWeight = document.getElementById('updateBodyStats').elements.namedItem("bodyStatWeight").value;
    //const bodyWeightUnit = document.getElementById('updateBodyStats').elements.namedItem("unitWeight").value;
    let bodyHeight = document.getElementById('updateBodyStats').elements.namedItem("bodyStatHeight").value;
    //const bodyHeightUnit = document.getElementById('updateBodyStats').elements.namedItem("unitHeight").value;
    const bodyStatsDate = document.getElementById('updateBodyStats').elements.namedItem("bodyStatDate").value;

    //console.log("Weight: " + bodyWeight + " " + bodyHeightUnit + "\nHeight: " + bodyHeight + " " + bodyWeightUnit + "\nDate: " + bodyStatsDate);
    //console.log("Weight: " + bodyWeight + "\nHeight: " + bodyHeight+ "\nDate: " + bodyStatsDate);

    if (bodyHeight <= 135 || bodyHeight >= 200 ) {
        alert("Please enter in a valid height");
    }

    if (bodyWeight <= 35 || bodyWeight >= 200) {
        alert("Please enter in a valid weight");
    }
/*
    if (bodyWeightUnit === "lb") {
        const bodyWeightTemp = (bodyWeight * 2.205);
        bodyWeight = bodyWeightTemp.toFixed(2);
    }

    if (bodyHeightUnit === "inches") {
        const bodyHeightTemp = (bodyHeight * 2.54);
        bodyHeight = bodyHeightTemp.toFixed(2);
    }
*/
    const bodyStatsBMI = calculateBMI(bodyHeight, bodyWeight);
    //console.log(bodyStatsBMI);

    let updatedBodyStats = {
        "weight": bodyWeight,
        "height": bodyHeight,
        "date": bodyStatsDate,
        "BMI": bodyStatsBMI
    };

    let updatedBodyStatsJSON = JSON.stringify(updatedBodyStats);

    //console.log(updatedBodyStats);
    //console.log(updatedBodyStatsJSON);

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

