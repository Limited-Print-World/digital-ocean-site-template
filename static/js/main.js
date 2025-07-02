        const ambient = document.getElementById('ambient');
        const bell = document.getElementById('bell');

        // Wait for user interaction to comply with browser autoplay policies
        document.body.addEventListener('click', () => {
            ambient.play();
        }, { once: true });

        // Play bell every 30 seconds
        setInterval(() => {
            bell.play();
        }, 35000);