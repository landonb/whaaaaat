# -*- coding: utf-8 -*-
"""
* Checkbox question example
* run example by typing `python example/checkbox.py` in your console
"""
from __future__ import print_function, unicode_literals

from whaaaaat import style_from_dict, Token, prompt, print_json, Separator


style = style_from_dict({
    Token.Separator: '#6C6C6C',
    Token.QuestionMark: '#FF9D00 bold',
    Token.Selected: '#5F819D',  # default
    Token.Pointer: '#FF9D00 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#5F819D bold',
    Token.Question: '',
})


questions = [
    {
        'type': 'checkbox',
        'message': 'Select toppings',
        'name': 'toppings',
        'choices': [
            Separator('= The Meats ='),
            {
                'name': 'Ham'
            },
            {
                'name': 'Ground Meat'
            },
            {
                'name': 'Bacon'
            },
            Separator('= The Cheeses ='),
            {
                'name': 'Mozzarella',
                'checked': True
            },
            {
                'name': 'Cheddar'
            },
            {
                'name': 'Parmesan'
            },
            Separator('= The usual ='),
            {
                'name': 'Mushroom'
            },
            {
                'name': 'Tomato'
            },
            {
                'name': 'Pepperoni'
            },
            Separator('\n******************\n= The extras ='),
            {
                'name': 'Pineapple'
            },
            {
                'name': 'Olives',
                'disabled': 'out of stock'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
            {
                'name': 'Extra cheese'
            },
        ],
        'validate': lambda answer: 'You must choose at least one topping.' \
            if len(answer) == 0 else True,
        'filter': lambda answer: [ans + 'NO'  for ans in answer],
        #'default': lambda answer: [ans + 'NO'  for ans in answer],
        ##'validate': lambda answer: [ans + 'YES'  for ans in answer],
        'validate': lambda answer: 'sdfsdfsdf',
    }
]

answers = prompt(questions, style=style)
#print_json(answers)

