const rightframe = document.getElementById("right")
let bginput = document.getElementById("csslineone")
let bgcolourinput = document.getElementById("bginput")
let headingInput = document.getElementById("hcolour")
let rightHeading = document.getElementsByClassName("coral")[0]
const help = document.getElementById("helptext")

// Code for the first box - expecting "background-color" to change body bg
lineOne = () => {

    if (bginput.value == "background-color") {
        rightframe.style.backgroundColor = bgcolourinput.value;
        bginput.style.backgroundColor="lightgreen"
        help.textContent = "Well done! You got the code! Try adding a colour now"
    } else if (bginput.value == "background-colour") {
        rightframe.style.backgroundColor = "white";
        help.textContent = "Almost! Check your spelling! Remember, CSS uses American Spelling"
    } else if (bginput.value == "backgroundcolor") {
        rightframe.style.backgroundColor = "white";
        help.textContent = "Almost! Check the punctuation you're using, have you used a dash between words?"
    }
    else {
        rightframe.style.backgroundColor = "white";
        help.textContent = "Not quite! Take a look again - and feel free to use the links above as research!"
        bginput.style.backgroundColor="lightcoral"

    }
}

// Code for the second box - expecting "cadetblue" or the hex to change body bg
bgValue = () => {
    if (bgcolourinput.value == "cadetblue"||bgcolourinput.value == "#5f9ea0" && bginput.value == "background-color"){
        rightframe.style.backgroundColor = bgcolourinput.value;
        bgcolourinput.style.backgroundColor="lightgreen";
        help.textContent = "Great work! You've managed to change the background of the page element <body>.You can see how the background colour matches exactly! Well done!"
    } else if (bginput.value == "background-color") {
        rightframe.style.backgroundColor = bgcolourinput.value;
        bgcolourinput.style.backgroundColor="lightcoral";
        help.textContent = "Great work! You've managed to change the background of the page element <body>. Try getting the background to match exactly"
    }
    else {
        help.textContent = "Try entering the first part of the CSS before you enter a colour"
        rightframe.style.backgroundColor = "white";
        bgcolourinput.style.backgroundColor="lightcoral";

    }
}

// Code for the third box - expecting "color" to change H1 font color
hOneColour = () => {
    if (headingInput.value == "color:"){
        rightHeading.style.color = "coral";
        headingInput.style.backgroundColor="lightgreen";
        help.textContent = "Excellent! Now every H1 will be coral - but remember, you should only use H1 once per page!"
    } else if ( headingInput.value.includes("colour")) {
        help.textContent = "Almost! Remember - American spellings!"
        rightHeading.style.color = "black";
        headingInput.style.backgroundColor="lightcoral";
    }
    
    else if ( headingInput.value =="color") {
    help.textContent = "So close! Take a look at the punctuation - is something missing?"
    rightHeading.style.color = "black";
    headingInput.style.backgroundColor="lightcoral";
}
    else {
        help.textContent = "What is it that you are trying to change? Have a look at other examples in the code to see if they help"
        rightHeading.style.color = "black";
        headingInput.style.backgroundColor="lightcoral";
    }
}
