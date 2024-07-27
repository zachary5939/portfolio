document.addEventListener("DOMContentLoaded", function () {
    const images = [
      { src: "image/portfolio/ToonFestWeb.gif", duration: 23300 }, // Duration in milliseconds
      { src: "image/portfolio/UNM.gif", duration: 26200 }
    ];
    const imageElement = document.getElementById("portfolio-image");

    let currentImageIndex = 0;

    function switchImage() {
      currentImageIndex = (currentImageIndex + 1) % images.length;
      imageElement.src = images[currentImageIndex].src;
      setTimeout(switchImage, images[currentImageIndex].duration);
    }

    // Start switching images
    setTimeout(switchImage, images[currentImageIndex].duration);
  });
