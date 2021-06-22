{
    name: '{[ model.label ]}',
    path: '/antd/{[ model._parent.name ]}/{[ model.name ]}/',
    routes: [
        // 增
        {
            name: '新增{[ model.label ]}',
            path: '/antd/{[ model._parent.name ]}/{[ model.name ]}/create',
            component: './{[ model._parent.name ]}/{[ model.name ]}/create.tsx',
            hideInMenu:true,
        },
        // 改
        {
            name: '权限{[ model.label ]}',
            path: '/antd/{[ model._parent.name ]}/{[ model.name ]}/update',
            component: './{[ model._parent.name ]}/{[ model.name ]}/update.tsx',
            hideInMenu:true,
        },
        // 查
        {
            name: '{[ model.label ]}详情',
            path: '/antd/{[ model._parent.name ]}/{[ model.name ]}/detail',
            component: './{[ model._parent.name ]}/{[ model.name ]}/detail.tsx',
            hideInMenu:true,
        },
        // 列表
        {
            name: '{[ model.label ]}列表',
            path: '/antd/{[ model._parent.name ]}/{[ model.name ]}/list',
            component: './{[ model._parent.name ]}/{[ model.name ]}/index.tsx',
        },
    ]
},