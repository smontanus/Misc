function newImage() {
    /* Function to randomly load a background
       image for a webpage. */
    currentIndx = 0;
    // Load Array of image file names.
    MyImages = new Array();
    MyImages[0] = 'images/slide01.jpg';
    MyImages[1] = 'images/slide02.jpg';
    MyImages[2] = 'images/slide03.jpg';
    MyImages[3] = 'images/slide04.jpg';
    MyImages[4] = 'images/slide05.jpg';
    MyImages[5] = 'images/slide06.jpg';
    MyImages[6] = 'images/slide07.jpg';
    loadImage = new Image(1024,352)
    // Generate a random index, load and display the image.
    currentIndx = Math.round(Math.random()*6)
    loadImage.src = MyImages[currentIndx]
    document.getElementById("slides").src = loadImage.src
}