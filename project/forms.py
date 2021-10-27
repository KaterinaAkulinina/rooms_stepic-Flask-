from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, SubmitField
from wtforms.validators import NumberRange, DataRequired


class gameForm(FlaskForm):
    way = SelectField(
        'Выберите сторону света, в которую желаете отправиться',
        coerce=int,
        choices=[
            (0, 'Север'),
            (1, 'Восток'),
            (2, 'Юг'),
            (3, 'Запад'),
        ],
    )
    number_steps = IntegerField(
        'Как далеко планируете продвинуться?',
        validators=[NumberRange(min=1), DataRequired()],
        default=1
    )
    sub = SubmitField("В путь!")