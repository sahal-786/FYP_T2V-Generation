$(document).ready(function() {
    $('#generate-form').submit(function(event) {
        event.preventDefault(); // Prevent default form submission

        var textPrompt = $('#text-prompt').val(); // Get text prompt from textarea

        // Show processing block
        $('#processing-block').show();

        // Send AJAX request to generate video
        $.ajax({
            type: 'POST',
            url: '/generate_video',
            data: { text_prompt: textPrompt },
            xhr: function() {
                var xhr = new window.XMLHttpRequest();
                // Upload progress
                xhr.upload.addEventListener("progress", function(evt){
                    if (evt.lengthComputable) {
                        var percentComplete = evt.loaded / evt.total;
                        // Update progress bar
                        $('#progress-bar').css('width', percentComplete*100 + '%');
                    }
                }, false);
                return xhr;
            },
            success: function(response) {
                // Hide processing block
                $('#processing-block').hide();
                
                // Display generated video
                $('#video-container').show();
                $('#generated-video').attr('src', response);
                
                // Set download link
                $('#download-button').attr('href', response);
            },
            error: function(xhr, status, error) {
                // Handle error
                console.error('Error:', error);
                // Hide processing block
                $('#processing-block').hide();
                // Show error message
                alert('An error occurred while generating the video.');
            }
        });
    });
});
