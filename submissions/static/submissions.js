function pad(number) {
  return number.toString().padStart(2, '0');
}

function updateTimer() {
    let seconds = timeDifference / 1000;

    let minutes = Math.floor(seconds / 60);
    seconds = Math.floor(seconds % 60);

    let hours = Math.floor(minutes / 60);
    minutes = Math.floor(minutes % 60);

    const element = document.getElementById("countdown-timer");
    if ((hours+minutes+seconds) > 0){
        element.innerHTML = hours + ":" + pad(minutes)  + ":" + pad(seconds);
    }
    else {
        element.innerHTML = 'Time Up'
    }

    timeDifference -= 1000;
}

setInterval(updateTimer, 1000);

window.onload = function() {
    updateTimer()
};



