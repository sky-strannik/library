// Кодировщик Base64

// Кодировщик
string text = project.Variables["text"].Value;
return Convert.ToBase64String(Encoding.UTF8.GetBytes(text)); // Base64 Encode

// Декодировщик
string base64String = project.Variables["base64String"].Value;
return Encoding.UTF8.GetString(Convert.FromBase64String(base64String)); // Base64 Decode