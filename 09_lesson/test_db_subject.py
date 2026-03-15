from sqlalchemy import create_engine, text


# Замените данные в строке подключения:
# myuser - имя пользователя для подключения к базе данных (введите свои данные)
# mypassword - пароль для подключения к базе данных (введите свои данные)
# localhost - адрес хоста, на котором находится база данных
# 5432 - порт, на котором работает сервер базы данных
#   (по умолчанию 5432, но проверьте какой указан у вас)
# mydatabase - имя базы данных,
#   к которой вы хотите подключиться (укажите имя своей БД)


db_connection_string = \
    "postgresql://myuser:mypassword@localhost:5432/mydatabase"
db = create_engine(db_connection_string)


# Проверяем добавление нового предмета
def test_insert_subject():
    connection = db.connect()
    transaction = connection.begin()

    # Создаём новый предмет
    new_id = 17
    new_title = 'Logic'

    sql_insert = text("INSERT INTO subject (\"subject_id\", "
                      "\"subject_title\") VALUES (:new_id, :new_title)")
    connection.execute(
        sql_insert, {'new_id': new_id, 'new_title': new_title})

    # Проверяем, что предмет добавлен: делаем SELECT
    sql_select = text(
        "SELECT subject_title FROM subject WHERE subject_id = :new_id")
    result = connection.execute(sql_select,
                                {'new_id': new_id}).mappings()
    row = result.fetchone()

    # Убеждаемся, что запись найдена и данные корректны
    assert row is not None, "Запись не найдена после вставки"
    assert row['subject_title'] == new_title, \
        f"Ожидалось '{new_title}', получено '{row['subject_title']}'"

    # Удаляем за собой новый предмет
    sql_delete = text("DELETE FROM subject WHERE subject_id = :new_id")
    connection.execute(sql_delete, {'new_id': new_id})

    transaction.commit()
    connection.close()


# Изменяем название предмета
def test_edit_subject():
    connection = db.connect()
    transaction = connection.begin()

    # добавляем новый предмет
    new_id = 17
    new_title = 'Logic'
    updated_title = 'Changed name'

    sql_insert = text("INSERT INTO subject (\"subject_id\", "
                      "\"subject_title\") VALUES (:new_id, :new_title)")
    connection.execute(sql_insert, {'new_id': new_id, 'new_title': new_title})

    # Меняем название
    sql_update = text(
        "UPDATE subject SET subject_title = :new_title WHERE subject_id = :id")
    connection.execute(
        sql_update, {"new_title": updated_title, "id": new_id})

    # Проверяем результат обновления: делаем SELECT
    sql_select = text(
        "SELECT subject_title FROM subject WHERE subject_id = :new_id")
    row = connection.execute(
        sql_select, {'new_id': new_id}).mappings().fetchone()

    # Убеждаемся, что запись найдена и данные корректны
    assert row is not None, "Запись не найдена после обновления"
    assert row['subject_title'] == updated_title, \
        f"Ожидалось '{updated_title}', получено '{row['subject_title']}'"

    # Удаляем за собой предмет
    sql_delete = text("DELETE FROM subject WHERE subject_id = :new_id")
    connection.execute(sql_delete, {"new_id": new_id})

    # Проверяем, что запись действительно удалена из БД
    verification_row = connection.execute(
        sql_select, {'new_id': new_id}).mappings().fetchone()
    assert verification_row is None, \
        f"Запись с ID {new_id} всё ещё существует после удаления"

    transaction.commit()
    connection.close()
