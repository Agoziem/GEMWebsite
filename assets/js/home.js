mapboxgl.accessToken = 'pk.eyJ1Ijoib2tmcyIsImEiOiJjbDFodTNjMG8wNnh6M2tycHN0ZDhzamYzIn0.H1VgtMiBAjkMEe7GXREzvA';
var map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/streets-v11',
  center: [6.800465, 6.124938],
  zoom: 12,
});


// Check if the user is anonymous (you can modify this condition based on your authentication system)
if (user === 'AnonymousUser') {
  // Set the time delay for showing the modal (10 minutes = 600000 milliseconds)
  const timeDelay = 20000;

  // Function to show the modal
  const showModal = () => {
    // Select the modal element by its ID
    const modal = document.getElementById('LoginModal');
  
    // Create a Bootstrap Modal instance
    const modalInstance = new bootstrap.Modal(modal);
  
    // Show the modal
    modalInstance.show();
  };

  // Set a timeout to trigger the modal after the time delay
  setTimeout(showModal, timeDelay);
}
