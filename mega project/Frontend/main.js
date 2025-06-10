


const sBtn = document.getElementById("ChatBtn");
const chatbox = document.getElementById("chatbox");







const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();

recognition.lang = 'en-US';
recognition.continuous = true;
recognition.interimResults = true;

let isListening = false;
let finalTranscript = '';
let isSpeaking = false; // prevents listening during TTS
const output = document.getElementById("output");
const toggleBtn = document.getElementById("MicBtn");
const li = document.getElementById("li");
const like = document.getElementById("like");


sBtn.addEventListener("click", getText);
chatbox.addEventListener("keypress", function (event) {
  if (event.key === "Enter") {
    getText();
  }
});


function getText() {
  // var text = document.getElementById("chatbox").value;
  const text = chatbox.value.trim(); // Get the trimmed value of the chatbox
  if (text === "") {
    return; // Do nothing if the input is empty
  }
  chatbox.value = "";
  output.innerText = text;
  like.innerText = "";
  console.log(text);
  eel.S(text)(callBack2)


}

function callBack2(data) {
  // eel.speak(data)()
  speaking(data);
  document.getElementById("get").innerText = data;

}


function callBack(data) {
  // eel.speak(data)()
  speak(data);
  document.getElementById("get").innerText = data;
  // r=data;
}




onload = () => {
  if (!isListening) {
    startRecognition();
    li.style.display = "block";
  } else {
    recognition.stop();
    isListening = false;
    li.style.display = "none";
  }
};

function startRecognition() {
  recognition.start();
  isListening = true;
}

recognition.onresult = (event) => {
  let interim = '';
  for (let i = event.resultIndex; i < event.results.length; ++i) {
    if (event.results[i].isFinal) {
      const text = event.results[i][0].transcript.trim();
      finalTranscript += text + "\n";
      // li.textContent = finalTranscript;
      if (text.toLowerCase().includes("friday")) {
        eel.S(text)(callBack)
        console.log("Recognized text:", text);
        // handleFinalText(text);
        output.innerText = text.toLowerCase();
      } // Update the like element with the recognized text
    } else {
      interim += event.results[i][0].transcript;
    }
  }
  // if (text.toLowerCase().includes("friday")) {
    output.textContent = interim;
  // }
};

recognition.onend = () => {
  if (isListening && !isSpeaking) {
    setTimeout(() => {
      recognition.start();
    }, 1000); // rest time
  }
};

recognition.onerror = (event) => {
  console.error("Speech error:", event.error);
};

// TEXT-TO-SPEECH helper to avoid recognizing its own output
function speak(text) {
  tc.textContent = "Ansering...";
  isSpeaking = true;
  recognition.stop(); // stop listening during speech

  const utter = new SpeechSynthesisUtterance(text);
  const voices = speechSynthesis.getVoices();

  // Try to find a natural-sounding female voice
  const preferredVoice = voices.find(voice =>
    voice.name === "Microsoft Aria Online (Natural)" ||
    voice.name === "Microsoft Jenny Online" ||
    voice.name.includes("Microsoft") && voice.name.toLowerCase().includes("female")
  );

  if (preferredVoice) {
    utter.voice = preferredVoice;
    console.log("Using voice:", preferredVoice.name);
  } else {
    console.log("Default voice used.");
  }

  utter.lang = 'en-US';
  utter.rate = 1;
  utter.pitch = 1;

  utter.onend = () => {
    console.log("Speech ended.");
    isSpeaking = false;
    tc.textContent = "Listening....";
    recognition.start(); // Resume listening
  };

  speechSynthesis.speak(utter);
}







function speaking(text) {
  isSpeaking = true;
  recognition.stop(); // stop listening during speech

  const utter = new SpeechSynthesisUtterance(text);
  const voices = speechSynthesis.getVoices();

  // Try to find a natural-sounding female voice
  const preferredVoice = voices.find(voice =>
    voice.name === "Microsoft Aria Online (Natural)" ||
    voice.name === "Microsoft Jenny Online" ||
    voice.name.includes("Microsoft") && voice.name.toLowerCase().includes("female")
  );

  if (preferredVoice) {
    utter.voice = preferredVoice;
    console.log("Using voice:", preferredVoice.name);
  } else {
    console.log("Default voice used.");
  }

  utter.lang = 'en-US';
  utter.rate = 1;
  utter.pitch = 1;

  utter.onend = () => {
    console.log("Speech ended.");
    isSpeaking = false;
    // recognition.start(); // Resume listening
  };

  speechSynthesis.speak(utter);
}




// // 🔁 You get clean sentence here
function handleFinalText(text) {
  eel.S(text)(callBack)
}


