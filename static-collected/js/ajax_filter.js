// Wait for the document to be ready
$(document).ready(function () {
    // Function to update the teacher list based on filters
    function updateTeacherList() {
        const letterFilter = $('#letter-filter').val();
        const subjectFilter = $('#subject-filter').val();

        // Send an AJAX request to the server to filter teachers
        $.ajax({
            url: '/teachers/filter/',  // Replace with the actual URL for your filter view
            method: 'GET',
            data: {
                letter: letterFilter,
                subject: subjectFilter,
            },
            success: function (data) {
                // Clear the teacher list
                console.log("hhhhhhhhhh",data,data.teachers);

                $('#teacher-list').empty();

                // Append each teacher to the list
                for (const teacher of data.teachers) {
                    const listItem = $('<li>');
                    listItem.append($('<a>', {
                        href: `/teachers/${teacher.id}/`,  // Replace with the actual URL for teacher profiles
                        text: `${teacher.first_name} ${teacher.last_name}`,
                    }));
                    $('#teacher-list').append(listItem);
                }
            },
            error: function (error) {

                console.error('Error:', error);
            },
        });
    }

    // Event listeners for filter inputs
    $('#letter-filter').on('input', updateTeacherList);
    $('#subject-filter').on('change', updateTeacherList);

    // Initial teacher list update on page load
    updateTeacherList();
});
