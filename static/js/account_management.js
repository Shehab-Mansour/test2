// Function to preview and update profile image
function loadFile(event) {
    var image = document.getElementById('profileImage');
    image.src = URL.createObjectURL(event.target.files[0]);
}
