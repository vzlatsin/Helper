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
    const addItemToInbox = (description) => {
        const listItem = document.createElement('li');
        listItem.textContent = description;
        inboxList.appendChild(listItem);
    };

    // Event listener for form submission
    captureForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const description = document.getElementById('capture-description').value;

        try {
            const response = await fetch('/unified-inbox', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ description }),
            });

            if (response.ok) {
                const data = await response.json();
                // Add item to the Unified Inbox
                addItemToInbox(description);
                console.log("Item added:", data);
            } else {
                console.error("Error adding item to inbox:", response.statusText);
            }
        } catch (error) {
            console.error("Error adding item to inbox:", error);
        }

        // Reset the form and close the modal
        captureForm.reset();
        closeModal();
    });
});
