# Lav en grundstruktur for en interaktiv hjemmeside om Thorium Initiative
# Dette kan bruges som kreativt produkt til EU Case Competition

html_content = """<!DOCTYPE html>
<html lang="da">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thorium Initiative - EU's Vej til Energiuafhængighed</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            color: white;
            overflow-x: hidden;
        }
        
        header {
            text-align: center;
            padding: 50px 20px;
            background: rgba(0, 0, 0, 0.3);
        }
        
        h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
            color: #ffd700;
        }
        
        .subtitle {
            font-size: 1.2rem;
            color: #e0e0e0;
            margin-bottom: 30px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .timeline {
            position: relative;
            padding: 50px 0;
        }
        
        .timeline-item {
            display: flex;
            align-items: center;
            margin: 40px 0;
            opacity: 0;
            transform: translateX(-50px);
            transition: all 0.6s ease;
        }
        
        .timeline-item.visible {
            opacity: 1;
            transform: translateX(0);
        }
        
        .timeline-content {
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 15px;
            flex: 1;
            margin-left: 20px;
            cursor: pointer;
            transition: transform 0.3s ease;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        .timeline-content:hover {
            transform: scale(1.02);
            background: rgba(255, 215, 0, 0.1);
        }
        
        .phase-number {
            background: #ffd700;
            color: #1e3c72;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            font-weight: bold;
        }
        
        .phase-title {
            font-size: 1.4rem;
            color: #ffd700;
            margin-bottom: 10px;
        }
        
        .phase-details {
            display: none;
            margin-top: 15px;
            padding-top: 15px;
            border-top: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        .interactive-section {
            background: rgba(255, 255, 255, 0.1);
            padding: 40px;
            border-radius: 20px;
            margin: 40px 0;
            text-align: center;
        }
        
        .thorium-cycle {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px;
            margin: 30px 0;
            flex-wrap: wrap;
        }
        
        .cycle-step {
            background: rgba(255, 215, 0, 0.2);
            padding: 20px;
            border-radius: 10px;
            border: 2px solid #ffd700;
            transition: all 0.3s ease;
            cursor: pointer;
            min-width: 150px;
        }
        
        .cycle-step:hover {
            background: rgba(255, 215, 0, 0.3);
            transform: scale(1.05);
        }
        
        .cycle-step.active {
            background: rgba(255, 215, 0, 0.4);
            box-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
        }
        
        .arrow {
            font-size: 2rem;
            color: #ffd700;
        }
        
        .quiz-container {
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 15px;
            margin: 30px 0;
        }
        
        .question {
            font-size: 1.2rem;
            margin-bottom: 20px;
            color: #ffd700;
        }
        
        .options {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        
        .option {
            background: rgba(255, 255, 255, 0.1);
            padding: 15px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            border: 1px solid transparent;
        }
        
        .option:hover {
            background: rgba(255, 215, 0, 0.2);
            border-color: #ffd700;
        }
        
        .option.correct {
            background: rgba(0, 255, 0, 0.2);
            border-color: #00ff00;
        }
        
        .option.wrong {
            background: rgba(255, 0, 0, 0.2);
            border-color: #ff0000;
        }
        
        .btn {
            background: #ffd700;
            color: #1e3c72;
            padding: 15px 30px;
            border: none;
            border-radius: 8px;
            font-size: 1.1rem;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            margin: 10px;
        }
        
        .btn:hover {
            background: #ffed4e;
            transform: translateY(-2px);
        }
        
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }
        
        .stat-card {
            background: rgba(255, 255, 255, 0.1);
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            transition: transform 0.3s ease;
        }
        
        .stat-card:hover {
            transform: translateY(-5px);
        }
        
        .stat-number {
            font-size: 2.5rem;
            color: #ffd700;
            font-weight: bold;
            display: block;
        }
        
        .footer {
            background: rgba(0, 0, 0, 0.5);
            padding: 30px;
            text-align: center;
            margin-top: 50px;
        }
        
        @media (max-width: 768px) {
            .timeline-item {
                flex-direction: column;
                text-align: center;
            }
            
            .timeline-content {
                margin-left: 0;
                margin-top: 20px;
            }
            
            .thorium-cycle {
                flex-direction: column;
            }
            
            .arrow {
                transform: rotate(90deg);
            }
        }
        
        .hidden {
            display: none;
        }
        
        .visible {
            display: block;
            animation: fadeIn 0.5s ease-in;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>
    <header>
        <h1>⚛️ Thorium Initiative</h1>
        <p class="subtitle">EU's Vej til Energiuafhængighed gennem Thorium-232 Teknologi</p>
        <p><em>Herlufsholm Skole | 3.g STX Samfundsfag A | EU Case Competition 2025</em></p>
        <button class="btn" onclick="startJourney()">Start Rejsen 🚀</button>
    </header>

    <div class="container">
        <!-- Timeline Section -->
        <section id="timeline-section" class="hidden">
            <h2 style="text-align: center; margin-bottom: 30px; font-size: 2rem; color: #ffd700;">📅 Trin-for-Trin Implementering</h2>
            <div class="timeline">
                <div class="timeline-item">
                    <div class="phase-number">1</div>
                    <div class="timeline-content" onclick="toggleDetails(this)">
                        <h3 class="phase-title">Forskning & Udvikling (2026-2030)</h3>
                        <p>Etabler thorium-pilotprojekter i EU med fokus på sikkerhed og effektivitet.</p>
                        <div class="phase-details">
                            <p><strong>💰 Budget:</strong> 5-10 mia. euro fra Horizon Europe</p>
                            <p><strong>🎯 Mål:</strong> Validere thorium-232 → uran-233 konvertering</p>
                            <p><strong>🏢 Partnere:</strong> Frankrig, Sverige, Orano, Vattenfall</p>
                            <p><strong>📊 Resultat:</strong> Småskala reaktorer og sikkerhedsdata</p>
                        </div>
                    </div>
                </div>

                <div class="timeline-item">
                    <div class="phase-number">2</div>
                    <div class="timeline-content" onclick="toggleDetails(this)">
                        <h3 class="phase-title">Bygning & Integration (2031-2035)</h3>
                        <p>Opfør kommercielle thorium-reaktorer og integrer i EU's elnet.</p>
                        <div class="phase-details">
                            <p><strong>💰 Budget:</strong> 20-30 mia. euro fra Connecting Europe Facility</p>
                            <p><strong>🎯 Mål:</strong> 5-10 kommercielle reaktorer</p>
                            <p><strong>⚡ Integration:</strong> 730 mia. euro transmissionsnet</p>
                            <p><strong>🌍 Ressourcer:</strong> Prioritér EU thorium-reserver (Norge)</p>
                        </div>
                    </div>
                </div>

                <div class="timeline-item">
                    <div class="phase-number">3</div>
                    <div class="timeline-content" onclick="toggleDetails(this)">
                        <h3 class="phase-title">Skalering & Regulering (2036-2040)</h3>
                        <p>Vedtag lovgivning og skaler thorium til 10-15% af EU's energimix.</p>
                        <div class="phase-details">
                            <p><strong>📜 Lovgivning:</strong> Klassificer thorium som "grøn" energi</p>
                            <p><strong>💸 Subsidier:</strong> Incitamenter for medlemslande</p>
                            <p><strong>🎯 Mål:</strong> 10-15% af EU's energimix</p>
                            <p><strong>🔄 Komplementering:</strong> Stable baseload til sol/vind</p>
                        </div>
                    </div>
                </div>
            </div>
            <div style="text-align: center;">
                <button class="btn" onclick="showThoriumCycle()">Udforsk Thorium-Cyklus ⚛️</button>
            </div>
        </section>

        <!-- Thorium Cycle Section -->
        <section id="cycle-section" class="hidden">
            <div class="interactive-section">
                <h2 style="margin-bottom: 20px; color: #ffd700;">⚛️ Interaktiv Thorium-Cyklus</h2>
                <p style="margin-bottom: 30px;">Klik på hver fase for at se processen:</p>
                
                <div class="thorium-cycle">
                    <div class="cycle-step" onclick="showStepInfo(1)" data-step="1">
                        <h4>Thorium-232</h4>
                        <p>Naturligt isotop</p>
                    </div>
                    <div class="arrow">→</div>
                    <div class="cycle-step" onclick="showStepInfo(2)" data-step="2">
                        <h4>Neutron Absorption</h4>
                        <p>Bestråling</p>
                    </div>
                    <div class="arrow">→</div>
                    <div class="cycle-step" onclick="showStepInfo(3)" data-step="3">
                        <h4>Protactinium-233</h4>
                        <p>Mellemprodukt</p>
                    </div>
                    <div class="arrow">→</div>
                    <div class="cycle-step" onclick="showStepInfo(4)" data-step="4">
                        <h4>Uran-233</h4>
                        <p>Fissilt brændstof</p>
                    </div>
                    <div class="arrow">→</div>
                    <div class="cycle-step" onclick="showStepInfo(5)" data-step="5">
                        <h4>Energi + Mindre Affald</h4>
                        <p>Resultat</p>
                    </div>
                </div>
                
                <div id="step-info" style="margin-top: 30px; padding: 20px; background: rgba(255,215,0,0.1); border-radius: 10px; display: none;">
                    <h3 id="step-title"></h3>
                    <p id="step-description"></p>
                </div>
                
                <button class="btn" onclick="showStats()">Se Konsekvenser 📊</button>
            </div>
        </section>

        <!-- Stats Section -->
        <section id="stats-section" class="hidden">
            <div class="interactive-section">
                <h2 style="margin-bottom: 30px; color: #ffd700;">📊 Konsekvenser og Statistikker</h2>
                
                <div class="stats">
                    <div class="stat-card">
                        <span class="stat-number">58%</span>
                        <p>EU's nuværende energiimport</p>
                        <small>Kan reduceres med thorium</small>
                    </div>
                    <div class="stat-card">
                        <span class="stat-number">61 mia€</span>
                        <p>Besparelser siden 2019</p>
                        <small>Ved reduceret fossilimport</small>
                    </div>
                    <div class="stat-card">
                        <span class="stat-number">730 mia€</span>
                        <p>Transmissionsnet investering</p>
                        <small>Frem mod 2040</small>
                    </div>
                    <div class="stat-card">
                        <span class="stat-number">2050</span>
                        <p>Klimaneutralitet mål</p>
                        <small>Thorium bidrager med 0% CO₂</small>
                    </div>
                </div>
                
                <button class="btn" onclick="showQuiz()">Test Din Viden 🧠</button>
            </div>
        </section>

        <!-- Quiz Section -->
        <section id="quiz-section" class="hidden">
            <div class="interactive-section">
                <h2 style="margin-bottom: 30px; color: #ffd700;">🧠 Quiz: EU's Energiudfordringer</h2>
                
                <div class="quiz-container">
                    <div class="question" id="question">Hvad er EU's nuværende energiimportafhængighed?</div>
                    <div class="options" id="options">
                        <div class="option" onclick="selectAnswer(this, false)">A) 35%</div>
                        <div class="option" onclick="selectAnswer(this, false)">B) 45%</div>
                        <div class="option" onclick="selectAnswer(this, true)">C) 58%</div>
                        <div class="option" onclick="selectAnswer(this, false)">D) 72%</div>
                    </div>
                    <div id="quiz-feedback" style="margin-top: 20px; display: none;"></div>
                </div>
                
                <div style="text-align: center; margin-top: 30px;">
                    <button class="btn" onclick="nextQuestion()">Næste Spørgsmål ➡️</button>
                    <button class="btn" onclick="showConclusion()">Se Konklusion 🎯</button>
                </div>
            </div>
        </section>

        <!-- Conclusion Section -->
        <section id="conclusion-section" class="hidden">
            <div class="interactive-section">
                <h2 style="margin-bottom: 30px; color: #ffd700;">🎯 Konklusion</h2>
                <p style="font-size: 1.2rem; line-height: 1.6; margin-bottom: 20px;">
                    <strong>Thorium Initiative</strong> er en realistisk, bæredygtig løsning på EU's energiudfordringer. 
                    Ved at kombinere klimaneutralitet, forsyningssikkerhed og økonomisk vækst, kan EU blive 
                    verdensførende inden for ren atomenergi.
                </p>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 30px 0;">
                    <div style="background: rgba(0,255,0,0.1); padding: 20px; border-radius: 10px; border-left: 4px solid #00ff00;">
                        <h3 style="color: #00ff00; margin-bottom: 10px;">✅ Fordele</h3>
                        <ul style="list-style: none; padding: 0;">
                            <li>• Reduceret CO₂-udledning</li>
                            <li>• Mindre radioaktivt affald</li>
                            <li>• Øget energisikkerhed</li>
                            <li>• Job i grøn teknologi</li>
                        </ul>
                    </div>
                    <div style="background: rgba(255,215,0,0.1); padding: 20px; border-radius: 10px; border-left: 4px solid #ffd700;">
                        <h3 style="color: #ffd700; margin-bottom: 10px;">⚠️ Udfordringer</h3>
                        <ul style="list-style: none; padding: 0;">
                            <li>• Høje investeringsomkostninger</li>
                            <li>• Politisk modstand i nogle lande</li>
                            <li>• Behov for nye reguleringer</li>
                            <li>• Teknologisk udvikling påkrævet</li>
                        </ul>
                    </div>
                </div>
                
                <div style="text-align: center; margin-top: 40px;">
                    <p style="font-style: italic; margin-bottom: 20px;">
                        "EU kan lede den grønne energirevolution med thorium som nøgleteknologi"
                    </p>
                    <button class="btn" onclick="restartJourney()">Genstart Rejsen 🔄</button>
                </div>
            </div>
        </section>
    </div>

    <footer class="footer">
        <p>&copy; 2025 Herlufsholm Skole | EU Case Competition 2025</p>
        <p>Thorium Initiative - En bæredygtig fremtid for Europa ⚛️🌱</p>
        <p style="margin-top: 10px; font-size: 0.9rem; color: #ccc;">
            Lavet med ❤️ for en grønnere fremtid
        </p>
    </footer>

    <script>
        let currentQuestion = 0;
        const questions = [
            {
                question: "Hvad er EU's nuværende energiimportafhængighed?",
                options: ["35%", "45%", "58%", "72%"],
                correct: 2,
                explanation: "EU importerer omkring 58% af sit energibehov, primært fra Rusland, Norge og Algeriet."
            },
            {
                question: "Hvad er målet for EU's klimaneutralitet?",
                options: ["2030", "2040", "2050", "2060"],
                correct: 2,
                explanation: "EU sigter mod klimaneutralitet i 2050 som del af European Green Deal."
            },
            {
                question: "Hvad er den store fordel ved thorium sammenlignet med uran?",
                options: ["Billigere at mine", "Kortere affaldshalveringstid", "Højere energidensitet", "Lettere at transportere"],
                correct: 1,
                explanation: "Thorium producerer radioaktivt affald med kortere halveringstid, hvilket reducerer langsigtede miljørisici."
            }
        ];

        const stepInfo = {
            1: {
                title: "Thorium-232 (Naturligt Isotop)",
                description: "Thorium-232 er et naturligt forekommende radioaktivt isotop, der findes i større mængder end uran. EU har adgang til thorium-reserver i lande som Sverige og Norge."
            },
            2: {
                title: "Neutronabsorption",
                description: "Thorium-232 absorberer en neutron i reaktoren og bliver til thorium-233, som hurtigt henfalder til protactinium-233."
            },
            3: {
                title: "Protactinium-233 (Mellemprodukt)",
                description: "Dette ustabile isotop henfalder med en halveringstid på 27 dage til uran-233 - det fissile brændstof vi ønsker."
            },
            4: {
                title: "Uran-233 (Fissilt Brændstof)",
                description: "Uran-233 er fissilt og kan opretholde en kædereaktion. Det er mere effektivt end uran-235 og producerer mindre langlivet affald."
            },
            5: {
                title: "Energi + Mindre Affald",
                description: "Fission af uran-233 producerer energi og mindre radioaktivt affald med kortere halveringstid. Processen kan 'avle' mere brændstof end den forbruger."
            }
        };

        function startJourney() {
            document.getElementById('timeline-section').classList.remove('hidden');
            document.getElementById('timeline-section').classList.add('visible');
            
            // Animate timeline items
            setTimeout(() => {
                const items = document.querySelectorAll('.timeline-item');
                items.forEach((item, index) => {
                    setTimeout(() => {
                        item.classList.add('visible');
                    }, index * 300);
                });
            }, 100);
            
            // Scroll to timeline
            document.getElementById('timeline-section').scrollIntoView({ behavior: 'smooth' });
        }

        function toggleDetails(element) {
            const details = element.querySelector('.phase-details');
            if (details.style.display === 'block') {
                details.style.display = 'none';
            } else {
                details.style.display = 'block';
            }
        }

        function showThoriumCycle() {
            hideAllSections();
            document.getElementById('cycle-section').classList.remove('hidden');
            document.getElementById('cycle-section').classList.add('visible');
            document.getElementById('cycle-section').scrollIntoView({ behavior: 'smooth' });
        }

        function showStepInfo(step) {
            // Remove active class from all steps
            document.querySelectorAll('.cycle-step').forEach(el => el.classList.remove('active'));
            
            // Add active class to clicked step
            document.querySelector(`[data-step="${step}"]`).classList.add('active');
            
            // Show step info
            const info = stepInfo[step];
            document.getElementById('step-title').textContent = info.title;
            document.getElementById('step-description').textContent = info.description;
            document.getElementById('step-info').style.display = 'block';
        }

        function showStats() {
            hideAllSections();
            document.getElementById('stats-section').classList.remove('hidden');
            document.getElementById('stats-section').classList.add('visible');
            document.getElementById('stats-section').scrollIntoView({ behavior: 'smooth' });
        }

        function showQuiz() {
            hideAllSections();
            document.getElementById('quiz-section').classList.remove('hidden');
            document.getElementById('quiz-section').classList.add('visible');
            currentQuestion = 0;
            loadQuestion();
            document.getElementById('quiz-section').scrollIntoView({ behavior: 'smooth' });
        }

        function loadQuestion() {
            const q = questions[currentQuestion];
            document.getElementById('question').textContent = q.question;
            const options = document.getElementById('options');
            options.innerHTML = '';
            
            q.options.forEach((option, index) => {
                const div = document.createElement('div');
                div.className = 'option';
                div.textContent = `${String.fromCharCode(65 + index)}) ${option}`;
                div.onclick = () => selectAnswer(div, index === q.correct);
                options.appendChild(div);
            });
            
            document.getElementById('quiz-feedback').style.display = 'none';
        }

        function selectAnswer(element, isCorrect) {
            const options = document.querySelectorAll('.option');
            options.forEach(opt => {
                opt.onclick = null; // Disable further clicks
                if (opt === element) {
                    opt.classList.add(isCorrect ? 'correct' : 'wrong');
                }
            });
            
            const feedback = document.getElementById('quiz-feedback');
            const q = questions[currentQuestion];
            feedback.innerHTML = `
                <p style="color: ${isCorrect ? '#00ff00' : '#ff6b6b'};">
                    ${isCorrect ? '✅ Korrekt!' : '❌ Forkert!'}
                </p>
                <p>${q.explanation}</p>
            `;
            feedback.style.display = 'block';
        }

        function nextQuestion() {
            if (currentQuestion < questions.length - 1) {
                currentQuestion++;
                loadQuestion();
            } else {
                showConclusion();
            }
        }

        function showConclusion() {
            hideAllSections();
            document.getElementById('conclusion-section').classList.remove('hidden');
            document.getElementById('conclusion-section').classList.add('visible');
            document.getElementById('conclusion-section').scrollIntoView({ behavior: 'smooth' });
        }

        function restartJourney() {
            hideAllSections();
            document.querySelector('header').scrollIntoView({ behavior: 'smooth' });
        }

        function hideAllSections() {
            const sections = ['timeline-section', 'cycle-section', 'stats-section', 'quiz-section', 'conclusion-section'];
            sections.forEach(id => {
                const section = document.getElementById(id);
                section.classList.add('hidden');
                section.classList.remove('visible');
            });
        }

        // Smooth scrolling for all internal links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });

        // Add some interactive animations on scroll
        window.addEventListener('scroll', () => {
            const elements = document.querySelectorAll('.stat-card, .timeline-item');
            elements.forEach(el => {
                const elementTop = el.getBoundingClientRect().top;
                const elementVisible = 150;
                
                if (elementTop < window.innerHeight - elementVisible) {
                    el.style.opacity = '1';
                    el.style.transform = 'translateY(0)';
                }
            });
        });
    </script>
</body>
</html>"""

# Gem HTML-filen
with open('thorium-initiative.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ Interaktiv hjemmeside 'thorium-initiative.html' er blevet oprettet!")
print("\n📋 Næste trin:")
print("1. Gå til GitHub.com og opret et nyt repository")
print("2. Kald det f.eks. 'thorium-initiative-eu-case'")
print("3. Upload thorium-initiative.html filen")
print("4. Aktivér GitHub Pages i Settings > Pages")
print("5. Din hjemmeside vil være tilgængelig på: username.github.io/repository-name")
print("\n🎨 Features inkluderet:")
print("- Interaktiv tidslinje med faser")
print("- Thorium-cyklus simulator")
print("- Quiz om EU energi")
print("- Statistikker og konsekvenser")
print("- Responsivt design")
print("- Smooth animations")