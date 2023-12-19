document.addEventListener("DOMContentLoaded", function () {
    createFallingLeaves();
});

function createFallingLeaves() {
    const leavesContainer = document.querySelector('.falling-leaves-container');
    const numberOfLeaves = 50; // Adjust the number of leaves as needed

    for (let i = 0; i < numberOfLeaves; i++) {
        createLeaf(leavesContainer);
    }
}

function createLeaf(container) {
    const leaf = document.createElement("div");
    leaf.className = "falling-leaf";
    setPosition(leaf);
    container.appendChild(leaf);
}

function setPosition(element) {
    const randomX = Math.random();
    const randomY = Math.random();
    const vw = window.innerWidth;
    const vh = window.innerHeight;

    element.style.left = `${randomX * vw}px`;
    element.style.top = `${randomY * vh}px`;
}
