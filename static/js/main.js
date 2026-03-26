document.addEventListener('DOMContentLoaded', () => {
    const generateBtn = document.getElementById('generate-btn');
    const languageSelect = document.getElementById('language');
    const situationText = document.getElementById('situation');
    const resultContainer = document.getElementById('result-container');
    const dialogueOutput = document.getElementById('dialogue-output');

    let isGenerating = false;

    generateBtn.addEventListener('click', async () => {
        if (isGenerating) return;

        const language = languageSelect.value;
        const situation = situationText.value.trim();

        if (!situation) {
            alert("Give the cosmic gears a situation to work with.");
            return;
        }

        try {
            isGenerating = true;
            generateBtn.disabled = true;
            generateBtn.classList.add('loading');
            generateBtn.querySelector('span').textContent = 'GENERATING...';

            const response = await fetch('/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ language, situation }),
            });

            const data = await response.json();
            
            // Show result container
            resultContainer.classList.remove('hidden');
            resultContainer.scrollIntoView({ behavior: 'smooth', block: 'end' });
            
            // Iconic Typing Animation
            typeDialogue(data.dialogue);

        } catch (error) {
            console.error('Error:', error);
            alert('Something went wrong in the cosmic script.');
        } finally {
            isGenerating = false;
            generateBtn.disabled = false;
            generateBtn.classList.remove('loading');
            generateBtn.querySelector('span').textContent = 'GENERATE DIALOGUE';
        }
    });

    function typeDialogue(text) {
        dialogueOutput.textContent = '';
        let i = 0;
        // Dynamic speed: faster for longer text
        const baseSpeed = text.length > 200 ? 15 : 30; 
        
        function type() {
            if (i < text.length) {
                dialogueOutput.textContent += text.charAt(i);
                i++;
                // Add slight randomness for a more "organic" feel
                const randomDelay = Math.random() * 10;
                setTimeout(type, baseSpeed + randomDelay);
            }
        }
        type();
    }
});
