document.addEventListener('DOMContentLoaded', () => {
    const captureButton = document.getElementById('capture-button');
    const modal = document.getElementById('capture-modal');
    const closeButton = document.querySelector('.close-button');
    const captureForm = document.getElementById('capture-form');
    const inboxList = document.getElementById('unified-inbox-list');

    // Function to open the modal
    const openModal = () => {
        modal.style.display = 'block';
    };

    // Function to close the modal
    const closeModal = () => {
        modal.style.display = 'none';
    };

    // Event listener to open the modal when the capture button is clicked
    captureButton.addEventListener('click', openModal);

    // Event listener to close the modal when the close button is clicked
    closeButton.addEventListener('click', closeModal);

    // Event listener to close the modal when clicking outside of the modal content
    window.addEventListener('click', (event) => {
        if (event.target == modal) {
            closeModal();
        }
    });

    // Function to add a new item to the Unified Inbox
    const addItemToInbox = (description, id) => {
        const listItem = document.createElement('li');
        listItem.textContent = description;
        listItem.dataset.id = id;

        // Adding edit and delete icons
        const editIcon = document.createElement('i');
        editIcon.className = 'fas fa-pencil-alt';
        editIcon.style.marginLeft = '10px';
        editIcon.style.cursor = 'pointer';
        editIcon.addEventListener('click', () => editItem(id, description));

        const deleteIcon = document.createElement('i');
        deleteIcon.className = 'fas fa-times';
        deleteIcon.style.marginLeft = '10px';
        deleteIcon.style.cursor = 'pointer';
        deleteIcon.addEventListener('click', () => deleteItem(id));

        listItem.appendChild(editIcon);
        listItem.appendChild(deleteIcon);
        inboxList.appendChild(listItem);
    };

    // Event listener for form submission
    captureForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const description = document.getElementById('capture-description').value;

        // Send the new item to the backend
        fetch('/unified-inbox', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ description })
        }).then(response => response.json())
          .then(data => {
              if (data.id) {
                  // Add item to the Unified Inbox
                  addItemToInbox(description, data.id);
                  // Reset the form and close the modal
                  captureForm.reset();
                  closeModal();
              } else {
                  console.error('Error adding item to inbox:', data.error);
              }
          });
    });

    // Function to edit an item
    const editItem = (id, oldDescription) => {
        const newDescription = prompt('Edit the description:', oldDescription);
        if (newDescription) {
            // Perform the update on the server and update the UI
            fetch(`/unified-inbox/${id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ description: newDescription })
            }).then(response => {
                if (response.ok) {
                    document.querySelector(`li[data-id='${id}']`).firstChild.textContent = newDescription;
                } else {
                    console.error('Failed to update item');
                }
            });
        }
    };

    // Function to delete an item
    const deleteItem = (id) => {
        fetch(`/unified-inbox/${id}`, {
            method: 'DELETE'
        }).then(response => {
            if (response.ok) {
                document.querySelector(`li[data-id='${id}']`).remove();
            } else {
                console.error('Failed to delete item');
            }
        });
    };

    // Load existing items from the backend
    fetch('/unified-inbox')
        .then(response => response.json())
        .then(items => {
            items.forEach(item => addItemToInbox(item.description, item.id));
        });
});
