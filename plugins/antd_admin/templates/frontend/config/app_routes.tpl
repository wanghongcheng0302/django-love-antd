{
    path: '/antd/{[ app.name ]}',
    name: '{[ app.label ]}',
    routes:[
    {% for model_route in model_routes -%}
        {[ model_route ]}
    {% endfor -%}
    ]
},