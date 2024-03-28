const membersContainer = document.getElementById('members');
document.addEventListener("DOMContentLoaded", function() {
    fetch_API_get()

    let addMemberButton = document.getElementById("addMemberButton");
    addMemberButton.addEventListener('click', function() {
        display_form('Add');
    });
});

//GET request - get all members
function fetch_API_get() {
    console.log('fetch_API_get');
    fetch('http://localhost:5000/client', {
        method: 'GET'
    })
    .then(response => {
        if (!response.ok) { 
            throw new Error('Failed to fetch members');
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
        // Display member data on the screen
        data.forEach(member => {
            memberDiv = addMemberToDisplay(member)
            membersContainer.appendChild(memberDiv);
        });

    })
    .catch(error => {
        console.error('Error fetching members:', error);
    });
}

//#POST request - add new member
function fetch_API_post() {
    console.log('fetch_API_post')
    const memberForm = document.getElementById('memberForm');
    let formData = new FormData(memberForm);
    let jsonData = {};
    formData.forEach((value, key) => {
        jsonData[key] = value;
    });
    console.log(jsonData);

    fetch('http://localhost:5000/client', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to add member');
        }
        return response.json();
    })
    .then(data => {
        //add the new member to display
        memberDiv = addMemberToDisplay(jsonData);
        membersContainer.appendChild(memberDiv);
        memberForm.reset();
        remove_dislapy_form();
    })
    .catch(error => {
        console.error('Error adding member:', error);
    });
}

//#PUT request - update a member
function fetch_API_put() {
    console.log('fetch_API_put');
    
    //ebstract the data from the form
    let memberForm = document.getElementById('memberForm');
    let formData = new FormData(memberForm);
    let jsonData = {};
    let memberId = document.getElementById('id').value;
    jsonData['id'] = memberId;

    //pass the data form to jsonData
    formData.forEach((value, key) => {
        jsonData[key] = value;
    });
    console.log(jsonData)

    //#PUT request
    fetch('http://localhost:5000/client', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to update member');
        }
        return response.json();
    })
    .then(data => {
        //update the member on the display
        console.log('Member updated successfully:', data);
        removeMemberFromDisplay(memberId)
        memberDiv = addMemberToDisplay(jsonData);
        membersContainer.appendChild(memberDiv);
        memberForm.reset();
        remove_dislapy_form();
    })
    .catch(error => {
        console.error('Error updating member:', error);
    });
}

//DELETE request - delete a member
function deleteMember(memberId) {
    fetch(`http://localhost:5000/client/${memberId}`, {
        method: 'DELETE'
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to delete member');
        }
        return response.json();
    })
    .then(data => {
        //remove the meber from the display
        console.log(data);
        removeMemberFromDisplay(memberId);
    })
    .catch(error => {
        console.error('Error deleting member:', error);
    });
}

//display the form of add and update member
function display_form(type_button) {
    console.log('display_form')
    let addForm = document.getElementById('divMemberForm');
    let overlay = document.getElementById('overlay');
    let submitButton = document.getElementById('send');
    // submitButton.setAttribute('id', type_button);
    submitButton.setAttribute('value', type_button);
    addForm.style.display = 'block';
    overlay.style.display = 'block';
    submitButton.style.display = 'block';

    //if this is add member
    let memberForm = document.getElementById('memberForm');
    if (type_button === 'Add') {
        console.log('add')
        memberForm.removeEventListener('submit', fetch_API_put);
        memberForm.addEventListener('submit', fetch_API_post);
    }

    //if this is update member
    else if (type_button === 'Update') {
        console.log('update')
        memberForm.removeEventListener('submit', fetch_API_post);
        memberForm.addEventListener('submit', fetch_API_put);
    }
}

//remove display the form of add and update member
function remove_dislapy_form(){
    console.log('remove_dislapy_form')
    let addForm = document.getElementById('divMemberForm');
    let overlay = document.getElementById('overlay');
    let submitButton = document.getElementById('send');
    addForm.style.display = 'none';
    overlay.style.display = 'none';
    submitButton.style.display = 'none';
}

//function for update a member
function updateForm(member){
    console.log('updateForm')
    display_form('Update');
    displayUpdateForm(member);
}

// Create a new div element for a member
function addMemberToDisplay(member){
    const memberDiv = document.createElement('div');
    memberDiv.id = `member-${member.id}`; 
    memberDiv.classList.add('member');
    memberDiv.innerHTML = `
        <p>ID: ${member.id}</p>
        <p>Name: ${member.first_name} ${member.last_name}</p>
    `;
    //Add a button to see member details
    let viewDetailsButton = document.createElement('button');
    viewDetailsButton.classList.add('viewDetailsButton');
    viewDetailsButton.textContent = 'View Details';

    viewDetailsButton.addEventListener('click', function() {
        // Create a message with member details        
        let message = `
            Member ID: ${member.id}\n
            First Name: ${member.first_name}\n
            Last Name: ${member.last_name}\n
            Address: ${member.address}\n
            Date of Birth: ${member.date_of_birth}\n
            Telephone: ${member.telephone}\n
            Mobile Phone: ${member.mobile_phone}\n
            Vaccine 1 Date: ${member.vaccine_1_date}\n
            Vaccine 1 Manufacturer: ${member.vaccine_1_manufacturer}\n
            Vaccine 2 Date: ${member.vaccine_2_date}\n
            Vaccine 2 Manufacturer: ${member.vaccine_2_manufacturer}\n
            Vaccine 3 Date: ${member.vaccine_3_date}\n
            Vaccine 3 Manufacturer: ${member.vaccine_3_manufacturer}\n
            Vaccine 4 Date: ${member.vaccine_4_date}\n
            Vaccine 4 Manufacturer: ${member.vaccine_4_manufacturer}\n
            Positive Result Date: ${member.positive_result_date}\n
            Recovery Date: ${member.recovery_date}\n
        `;
        window.alert(message);
    });

    //add update, delete and view details buttons
    let deleteMemberButton = add_delete_button();
    let updateMemberButton = add_update_button();

    memberDiv.appendChild(deleteMemberButton);
    memberDiv.appendChild(updateMemberButton);
    memberDiv.appendChild(viewDetailsButton);  
    return memberDiv;


    //Add a button to delete member
    function add_delete_button(){   
        let deleteMemberButton = document.createElement('button');
        deleteMemberButton.classList.add('deleteMemberButton');
        deleteMemberButton.textContent = 'Delete Member';
        deleteMemberButton.addEventListener('click', function() {
        deleteMember(member.id); 
        });
        return deleteMemberButton;
    }

   // Add a button to update member
    function add_update_button(){
        let updateMemberButton = document.createElement('button');
        updateMemberButton.classList.add('updateMemberButton');
        updateMemberButton.textContent = 'Update Member';
        updateMemberButton.addEventListener('click', function() {
            updateForm(member);
            //displayUpdateForm(member);
        });
        return updateMemberButton;
    }
}

//Checking the correctness of the form input
function validateDates() {
    // Get the values of the date inputs
    let positiveResultDate = document.getElementById('positive_result_date').value;
    let recoveryDate = document.getElementById('recovery_date').value;
    let vaccine1Date = document.getElementById('vaccine_1_date').value;
    let vaccine2Date = document.getElementById('vaccine_2_date').value;
    let vaccine3Date = document.getElementById('vaccine_3_date').value;
    let vaccine4Date = document.getElementById('vaccine_4_date').value;
    let dateBirth = document.getElementById('date_of_birth').value;
    let formatDateBirth = new Date(dateBirth)

    //Checking that the date of birth is the earliest date
    if (new Date(positiveResultDate) < formatDateBirth || new Date(recoveryDate) < formatDateBirth || 
    new Date(vaccine1Date) < formatDateBirth || new Date(vaccine2Date) < formatDateBirth ||
    new Date(vaccine3Date) < formatDateBirth || new Date(vaccine4Date) < formatDateBirth)
    {
        alert('date of birth nust be the earlest data!');
        return false; 
    }

    // Check if positive result date is entered
    if (positiveResultDate.trim() !== '') {
        // If positive result date is entered, recovery date must also be entered
        if (recoveryDate.trim() === '') {
            alert('Please enter recovery date.');
            return false; 
        }

        // Check if recovery date is later than positive result date
        if (new Date(recoveryDate) < new Date(positiveResultDate)) {
            alert('Recovery date must be later than positive result date.');
            return false; 
        }
    }

    // Check vaccination dates
    if (new Date(recoveryDate) < new Date(positiveResultDate)) {
        alert('Recovery date must be later than positive result date.');
        return false; 
    }
    if (vaccine1Date.trim() === '' && vaccine2Date.trim() !== '') {
        alert('Please enter Vaccine Date 2.');
        return false; 
    }

    if (vaccine2Date.trim() === '' && vaccine3Date.trim() !== '') {
        alert('Please enter Vaccine Date 3.');
        return false;
    }

    if (vaccine3Date.trim() === '' && vaccine4Date.trim() !== '') {
        alert('Please enter Vaccine Date 4.');
        return false; 
    }

    // If all validations pass or if positive result date is not entered, allow form submission
    return true;
}

//remove the deleted member from the display
function removeMemberFromDisplay(memberId) {
    let memberDiv = document.getElementById(`member-${memberId}`);
    if (memberDiv) {
        memberDiv.remove();
    } else {
        console.error(`Member with ID ${memberId} not found.`);
    }
}

//update the form fields for update member
function displayUpdateForm(member) {
    let updateForm = document.getElementById('divMemberForm');
    updateForm.querySelector('#id').value = member.id;
    updateForm.querySelector('#first_name').value = member.first_name;
    updateForm.querySelector('#last_name').value = member.last_name;
    updateForm.querySelector('#address').value = member.address;
    updateForm.querySelector('#date_of_birth').value = ChangeToformatDate(member.date_of_birth);
    updateForm.querySelector('#telephone').value = member.telephone;
    updateForm.querySelector('#mobile_phone').value = member.mobile_phone;
    updateForm.querySelector('#vaccine_1_date').value = ChangeToformatDate(member.vaccine_1_date);
    updateForm.querySelector('#vaccine_1_manufacturer').value = ChangeNullToNoChoice(member.vaccine_1_manufacturer);
    updateForm.querySelector('#vaccine_2_date').value = ChangeToformatDate(member.vaccine_2_date);
    updateForm.querySelector('#vaccine_2_manufacturer').value = ChangeNullToNoChoice(member.vaccine_2_manufacturer);
    updateForm.querySelector('#vaccine_3_date').value = ChangeToformatDate(member.vaccine_3_date);
    updateForm.querySelector('#vaccine_3_manufacturer').value = ChangeNullToNoChoice(member.vaccine_3_manufacturer);
    updateForm.querySelector('#vaccine_4_date').value = ChangeToformatDate(member.vaccine_4_date);
    updateForm.querySelector('#vaccine_4_manufacturer').value = ChangeNullToNoChoice(member.vaccine_4_manufacturer);
    updateForm.querySelector('#positive_result_date').value = ChangeToformatDate(member.positive_result_date);
    updateForm.querySelector('#recovery_date').value = ChangeToformatDate(member.recovery_date);
    console.log(updateForm)
    updateForm.querySelector('#id').disabled = true;
}

//convert null to "no-choice"
function ChangeNullToNoChoice(vaccine_manufacturer) {
    if (vaccine_manufacturer === null) {
        return "no-choice"
    }
    else {
        return vaccine_manufacturer
    }
}

//convert the format date date to string
function ChangeToformatDate(dateString) {
    console.log(dateString)
    if (dateString !== null){
        let date = new Date(dateString);
        let year = date.getFullYear();
        let month = String(date.getMonth() + 1).padStart(2, '0'); 
        let day = String(date.getDate()).padStart(2, '0');
        return `${year}-${month}-${day}`;
    }
    else
        return null
}


