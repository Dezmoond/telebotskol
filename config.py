import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot Token
BOT_TOKEN = os.getenv("BOT_TOKEN")

# OpenAI API Key для агента-учителя (опционально)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Paths
DATA_PATH = "data/"
MEDIA_PATH = "media/"
AUDIO_PATH = "media/audio/"
IMAGES_PATH = "media/images/"
# --- Новые пути для моделей Piper ---
PIPER_MODELS_PATH = "piper_voices/" # Создайте эту папку
os.makedirs(PIPER_MODELS_PATH, exist_ok=True) # Убедитесь, что папка существует

# --- Настройки произношения ---
PRONUNCIATION_LOWER_THRESHOLD = 70.0 # Нижний порог для "хорошо, но можно лучше"
PRONUNCIATION_UPPER_THRESHOLD = 98.0 # Верхний порог для "отличное произношение"
WORD_COUNT_COEFFICIENT_MULTIPLIER = 0.5 # Коэффициент влияния на пороги (0 - нет влияния, 1 - макс. влияние)
WORD_COUNT_REFERENCE_WORDS = 7 # Количество слов, при котором влияние коэффициента отсутствует

# --- Настройки TTS голосов ---
DEFAULT_VOICE_NAME = "Amy"
# Словарь: Имя_голоса: (файл_модели, файл_конфигурации)
# Предполагаем, что модели будут находиться в PIPER_MODELS_PATH
AVAILABLE_VOICES = {
    "Amy": ("en_US-amy-medium.onnx", "en_US-amy-medium.onnx.json"),
    "Kristin": ("en_US-kristin-medium.onnx", "en_US-kristin-medium.onnx.json"),
    "Norman": ("en_US-norman-medium.onnx", "en_US-norman-medium.onnx.json"),
    "Joe": ("en_US-joe-medium.onnx", "en_US-joe-medium.onnx.json"),
    "Google TTS": ("gTTS", None) # Добавляем gTTS как опцию
}

# Messages (обновляем или добавляем новые, если нужно)
MESSAGES = {
    "welcome": "Привет! Давай изучать английский язык! 🇬🇧",
    "start_lesson": "Начинаем урок! 📚",
    "terms_intro": "Давай изучим следующие термины!\n\nЯ буду отправлять тебе термин на английском, картинку, транскрипцию и голосовое сообщение с произношением.\nИспользуй кнопку ниже для навигации.",
    "terms_complete": "Ты молодец! Все термины изучены! Двигаемся дальше!",
    "pronunciation_intro": "Я буду тебе произносить слово, а твоя задача постараться повторить за мной. Если никак не получается, просто жми клавишу «Пропустить»",
    "pronunciation_complete": "Супер, ты справился с произношением! Давай теперь запомним значения слов",
    "pronunciation_instruction": "Теперь запишите голосовое сообщение с произношением",
    "lexical_intro": "Выбери корректный перевод слова",
    "lexical_en_ru_complete": "Каждое новое слово — шаг вперёд! Теперь немного изменим задачу",
    "lexical_ru_en_complete": "Главное — прогресс, а не совершенство. Ты растёшь!",
    "grammar_intro": "А теперь самое время познакомиться с грамматикой",
    "grammar_understood": "Всё понятно ✅",
    "grammar_questions": "Есть вопросики ❓",
    "grammar_ask_question": "Задайте свой вопрос по грамматике текстом:",
    "grammar_now_understood": "Теперь всё понятно ✅",
    "grammar_still_questions": "Остались вопросы ❓",
    "grammar_complete": "Отлично! Грамматический блок пройден 📚",
    "teacher_thinking": "🤔 Подумаю над вашим вопросом...",
    # Лексико-грамматические упражнения
    "verb_exercise_intro": "Напечатайте пропущенный глагол в нужной временной форме",
    "verb_exercise_complete": "💪 Ты отлично справляешься — так держать!",
    "mchoice_intro": "Выберите правильный вариант ответа",
    "mchoice_complete": "Ещё одно упражнение — и ты ближе к цели!",
    "missing_word_intro": "Вставьте подходящее по смыслу пропущенное слово. Отправьте текстовое сообщение",
    "missing_word_complete": "Английский открывает двери — и ты их уже открываешь!",
    "negative_intro": "Переделайте предложение в отрицательную форму. Отправьте текстовое сообщение",
    "negative_complete": "Твой мозг обожает такую тренировку!",
    "question_intro": "Переделайте предложение в вопросительную форму. Отправьте текстовое сообщение",
    "question_complete": "Маленькие шаги приводят к большим результатам!",
    # Блок аудирования
    "listening_true_false_intro": "Прослушайте голосовое сообщение столько раз, сколько вам нужно для его понимания. Выберите корректный вариант ответа True «верно» или False «неверно»",
    "listening_choice_intro": "Прослушайте голосовое сообщение 2 раза. Выберите корректный вариант ответа",
    "listening_phrases_intro": "Прослушайте голосовое сообщение 2 раза, повторите фразу за спикером. Для продолжения, или если никак не получается, смело жмите клавишу 'Дальше'",
    "listening_true_false_complete": "Отличная работа! Продолжим в том же духе!",
    "listening_choice_complete": "Я знаю, что это было не так просто, но это часть пути",
    "listening_phrases_complete": "Сложные задачи делают тебя сильнее — и ты только что стал сильнее",
    # Удалены старые сообщения о произношении
    "true_answer": "Верно",
    "false_answer": "Неверно",
    # Блок письменной речи
    "writing_sentences_intro": "Составьте предложение с предлагаемым словом и напишите его, отправив текстовое сообщение",
    "writing_translation_intro": "Напишите перевод предложения на английский язык",
    "writing_sentences_complete": "Отлично! Переходим к переводу предложений",
    "writing_translation_complete": "🎉 Блок письменной речи завершен!",
    "writing_word_prompt": "Составьте предложение со словом:",
    "writing_translate_prompt": "Переведите на английский:",
    "continue_writing": "Продолжить урок",
    # Блок говорения
    "speaking_intro": "Подумайте над предложенной ситуацией и запишите голосовое сообщение с вашими размышлениями. \n📌 Длина — любая, столько, сколько сможете сказать.\n Когда будете готовы, нажмите кнопку «Записать мысли» и начните говорить",
    "speaking_situation": "Ситуация для обсуждения:",
    "speaking_instruction": "Запишите голосовое сообщение с вашими мыслями по этой теме:",
    "speaking_analyzing": "🔄 Анализирую ваше высказывание...",
    "speaking_complete": "🎉 Поздравляем! Вы завершили полный курс английского языка для программистов!",
    "speaking_final": "Мозг, конечно, подпотел... но ты прошёл это! Даже английский немного в шолке. Переходим к следующему уроку?",
    "record_speaking": "Записать мысли 🎤",
    "correct_answer": "✅ Правильно!",
    "wrong_answer": "❌ Упс, ошибка! Правильный ответ: ",
    "next_button": "Дальше ➡️",
    "skip_button": "Пропустить ⏭️",
    # Новые сообщения для произношения
    "pronunciation_perfect": "🎉 Отлично! Идеальное произношение!",
    "pronunciation_good_but_better": "👍 Хорошо, но можно улучшить!",
    "pronunciation_needs_practice": "⚠️ Требуется больше практики",
    "pronunciation_errors_found": "Отлично! Но обнаружены следующие ошибки произношения:",
    "voice_selection_intro": "Выберите голос для произношения:"
}

# Ensure directories exist
os.makedirs(AUDIO_PATH, exist_ok=True)
os.makedirs(IMAGES_PATH, exist_ok=True)