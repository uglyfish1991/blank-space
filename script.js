// Const Variables
const block = document.getElementsByClassName("container")

// Increase Difficulty options
let current = 0

const refresh = () => {
    console.log("refresh")
    for (let i = 0; i < block.length; i++) {
        block[i].style.display = "none"
    }
    block[current].style.display = "flex"
}

const add = () => {
    if (current < 4) {
        current ++
        console.log(current)
        refresh()
    }
}

// Maybe put the minus button back in? 
const minus = () => {
    if (current > 0) {
        current --
        console.log(current)
        refresh()
    }
}

// Level 1 Variables

const rightframe = document.getElementById("right") //Top right ID
let bginput = document.getElementById("bgsyntax")   // first empty box for "bg-color"
let bgcolourinput = document.getElementById("bginput") // second empty box, for actual value 
let headingInput = document.getElementById("hcolour") //third empty box, for H1 "color"
let rightHeading = document.getElementsByClassName("coral")[0] // H1 on right side that actually changes
let rightMiddle = document.getElementsByClassName("middle")[0] // middle div on right side that actually changes
let textDecoration = document.getElementById("tdunderline") //fourth empty box, for h1 "text decoration"
let middlePx = document.getElementById("pxsize") //fith empty box, for middle dix width unit "px"
let middleMar = document.getElementById("marright") //sixth empty box, expecting "right" for centering div"
let middleAlign = document.getElementById("midalign") //seventh empty box, expecting "center" for text align"
const help = document.getElementById("helptext1") // helptext at bottom of page




// Code for the first box - expecting "background-color" to change body bg
lineOne = () => {
    console.log("l1 function happening")
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
        bgcolourinput.style.backgroundColor="lightcoral"

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

// Code for the fourth box - expecting "text" to change decoration
tdUnderline = () => {
    if (textDecoration.value == "text"){
        rightHeading.style.textDecoration="underline";
        textDecoration.style.backgroundColor="lightgreen";
        help.textContent = "Excellent! We've decorated our H1  by underlining it! Now every instance of H1 will be underlined - but remember, you should only use H1 once per page!"
    } 
    else {
        help.textContent = "What is it that you are trying to change? Have a look at other examples in the code to see if they help"
        rightHeading.style.textDecoration="none";
        textDecoration.style.backgroundColor="lightcoral";
    }
}

// Code for the fifth box - expecting px to change width
pxSize = () => {
    if (middleMar.value == "right" && middlePx.value=="px"){
        rightMiddle.style.marginRight="auto";
        rightMiddle.style.width="400px";
        help.textContent = "Excellent! We made our div 400px wide! To center it, we need to tell the browser to auto-find the left and right margins, and display as 'block'. That was tough! Well done!"
        middlePx.style.backgroundColor="lightgreen";
        middleMar.style.backgroundColor="lightgreen";
    } else if (middlePx.value == "px"){
        rightMiddle.style.width="400px";
        middlePx.style.backgroundColor="lightgreen";
        help.textContent = "Excellent! We can use values to give our elements sizes. In this case, we've said we want the div class 'middle' to be 400px wide!"
    } else if (middlePx.value == "pixels" ||middlePx.value == "Pixels" ){
        help.textContent = "Pixels is correct! but we can write it a shorter way! Like you can shortned centimetres to cm, you can shorten pixels!"
        rightMiddle.style.width="100%";
        middlePx.style.backgroundColor="lightcoral";
    } else if (middlePx.value == "%" ||middlePx.value == "percent" ){
        help.textContent = "You've got the right idea! We need to give our browser a unit - 400 what? But 400% means 4 x the full width of the container it is in - that could be a little too big!"
        rightMiddle.style.width="400%";
        middlePx.style.backgroundColor="lightcoral";
    }
    else {
        help.textContent = "We've specified the property, and weve specified a number - should we be specific about the unit?"
        rightMiddle.style.width="100%";
        middlePx.style.backgroundColor="lightcoral";
    }
}

// Code for the fifth box - expecting px to change width
marR = () => {
    if (middleMar.value == "right" && middlePx.value=="px"){
        rightMiddle.style.marginRight="auto";
        help.textContent = "Excellent! We made our div 400px wide! To center it, we need to tell the browser to auto-find the left and right margins, and display as 'block'. That was tough! Well done!"
        middlePx.style.backgroundColor="lightgreen";
        middleMar.style.backgroundColor="lightgreen";

    } else if (middleMar.value == "right" && middlePx.value!="px"){
        help.textContent = "Your margin is correct - but you wont see a result just yet! You'll see the result better if the div isnt the whole width of the page!"
        middleMar.style.backgroundColor="lightcoral";
    } 
    else {
        help.textContent = "Is there anything else similar in the CSS? Any other positions/directions listed that we could use the opposite of?"
        rightMiddle.style.marginRight="0px";
        middleMar.style.backgroundColor="lightcoral";
    }
}

// Code for the seventh box - expecting center to change alignment
midAlign = () => {
    if (middleAlign.value == "center"){
        rightMiddle.style.textAlign="center";
        help.textContent = "Great work! We can align our text using text-align, and in this case, we've centred it. Well done for noticing the American spelling, too!"
        middleAlign.style.backgroundColor="lightgreen";

    } else if (middleAlign.value=="centre"){
        help.textContent = "So close! Remember, we use American spellings in the code!"
        middleAlign.style.backgroundColor="lightcoral";
    } 
    else {
        help.textContent = "How are we trying to align our text? It's currently aligned to the left"
        rightMiddle.style.textAlign="left";
        middleAlign.style.backgroundColor="lightcoral";
    }
}

fullCheck = () => {
    if (middleAlign.value == "center" && middleMar.value == "right" && middlePx.value=="px" && bginput.value == "background-color" && bgcolourinput.value == "cadetblue"||bgcolourinput.value == "#5f9ea0" &&textDecoration.value == "text" &&headingInput.value == "color:"){
        help.textContent = "Amazing work! Use the 'Next' button above to move on to a harder challenge!"
    }    }
