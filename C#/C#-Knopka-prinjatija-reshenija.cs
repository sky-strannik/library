// Создаем окно формы
System.Windows.Forms.Form F = new System.Windows.Forms.Form();
F.BringToFront();													// Поверх других окон
F.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
F.Text = "Выберите, что делать дальше...";							// Название окна
F.Width = 555;    													// Задает ширину окна в пикселях
F.Height = 200;    													// Задает высоту окна в пикселях

// Лейбл (Текст сообщения)
System.Windows.Forms.Label label = new System.Windows.Forms.Label();
label.Font = new System.Drawing.Font("Microsoft Sans Serif", 12.00F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 204);
label.Text = "Пожалуйста, укажите, что делать дальше?";
label.Location = new System.Drawing.Point(80,40);					// Позиция надписи
label.AutoSize=true;
F.Controls.Add(label);

// Тестовое текстовое поле (не забыть добавить поле в клики по кнопкам)
// System.Windows.Forms.TextBox textb = new System.Windows.Forms.TextBox();
// textb.Location = new System.Drawing.Point(50,50);
// textb.Width=200;
// F.Controls.Add(textb);

// Создаем кнопку
System.Windows.Forms.Button start = new System.Windows.Forms.Button();
start.Text = "Да";													// Текст на кнопке
start.Location = new System.Drawing.Point(80,90);					// Позиция кнопки
start.Size = new System.Drawing.Size(110, 35);						// Размер кнопки (ширина,высота)
start.Click+= delegate(object sender, System.EventArgs e)			// Событие для клика по кнопке
	{
        project.Variables["button"].Value = start.Text;				// Кладем в переменную
		F.Close();													// Закрываем окно, сохраняя значение
	}; 
F.Controls.Add(start);												// Добавляем бокс в форму

// Создаем кнопку
System.Windows.Forms.Button stop = new System.Windows.Forms.Button();
stop.Text = "Нет";													// Текст на кнопке
stop.Location = new System.Drawing.Point(215,90);					// Позиция кнопки
stop.Size = new System.Drawing.Size(110, 35);						// Размер кнопки (ширина,высота)
stop.Click+= delegate(object sender, System.EventArgs e)			// Событие для клика по кнопке
	{
        project.Variables["button"].Value = stop.Text;				// Кладем в переменную
		F.Close();													// Закрываем окно, сохраняя значение
	}; 
F.Controls.Add(stop);												// Добавляем бокс в форму

// Создаем кнопку
System.Windows.Forms.Button cancel = new System.Windows.Forms.Button();
cancel.Text = "Отмена";												// Текст на кнопке
cancel.Location = new System.Drawing.Point(350,90);					// Позиция кнопки
cancel.Size = new System.Drawing.Size(110, 35);						// Размер кнопки (ширина,высота)
cancel.Click+= delegate(object sender, System.EventArgs e)			// Событие для клика по кнопке
	{
        project.Variables["button"].Value = cancel.Text;			// Кладем в переменную
		F.Close();													// Закрываем окно, сохраняя значение
	}; 
F.Controls.Add(cancel);												// Добавляем бокс в форму

F.AcceptButton=start; 												// Отправка по enter
F.ShowDialog();														// Выводим форму на экран