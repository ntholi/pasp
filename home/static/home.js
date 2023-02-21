document.querySelectorAll('.clickable').forEach(it => {
    it.addEventListener("mouseover", function () {
        it.classList.add("border");
        it.classList.add("border-secondary");
    });
    it.addEventListener("mouseout", function () {
        it.classList.remove("border");
        it.classList.remove("border-secondary");
    });
})

const assessmentContainer = document.getElementById("assessment");
const assessmentTimer = document.getElementById("assessment-timer");

assessmentContainer.addEventListener("mouseenter", function () {


    let startTime = new Date(assessmentContainer.dataset.startTime);
    let currentTime = new Date();
    let timeDifference = startTime - currentTime;

    if (timeDifference > 0) {
        let minutesBeforeStart = Math.floor(timeDifference / 60000);
        assessmentTimer.innerHTML = `Come Back After ${minutesBeforeStart} minutes`;
        assessmentTimer.style.display = "block";
    }
});

assessmentContainer.addEventListener("mouseleave", function () {
    assessmentTimer.style.display = "none";
});
