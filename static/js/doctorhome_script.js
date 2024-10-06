document.addEventListener('DOMContentLoaded', function() {
    // Manage appointment form submission
    const submitBtn = document.querySelector('form button');
    if (submitBtn) {
        submitBtn.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent form submission
            const patientId = document.getElementById('patientId') ? document.getElementById('patientId').value : null;
            const appointmentDate = document.getElementById('appointmentDate') ? document.getElementById('appointmentDate').value : null;
            if (patientId && appointmentDate) {
                alert(`Appointment set for Patient ID: ${patientId} on ${appointmentDate}`);
            } else {
                alert('Please fill in all fields');
            }
        });
    }

    // Load warehouse inventory data
    const data = {
        totalItems: 324,
        totalCategories: 40,
        mostStocked: "Acrylic Paints"
    };

    document.getElementById('totalItems').textContent = data.totalItems;
    document.getElementById('totalCategories').textContent = data.totalCategories;
    document.getElementById('mostStocked').textContent = data.mostStocked;

    // Add functionality for the 'Add New Appointment' button
    const addAppointmentBtn = document.querySelector('.btn-primary');
    if (addAppointmentBtn) {
        addAppointmentBtn.addEventListener('click', function() {
            alert('Add New Appointment clicked!');
        });
    }

    // Add functionality for the 'Add New Patient' button
    const addPatientBtn = document.querySelector('.btn-secondary');
    if (addPatientBtn) {
        addPatientBtn.addEventListener('click', function() {
            alert('Add New Patient clicked!');
        });
    }
});


// تحديد الناف بار
const navbar = document.querySelector('.navbar');

// إضافة نافذة مراقبة التمرير
window.onscroll = function() {
    if (window.scrollY > 50) {
        navbar.classList.add('small-navbar');
    } else {
        navbar.classList.remove('small-navbar');
    }
};