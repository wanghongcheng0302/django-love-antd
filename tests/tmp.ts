export default [
  {
    path: '/',
    component: '../layouts/BlankLayout',
    routes: [
      {
        path: '/user',
        component: '../layouts/UserLayout',
        routes: [
          {
            name: 'login',
            path: '/user/login',
            component: './User/login',
          },
        ],
      },
      {
        path: '/',
        component: '../layouts/SecurityLayout',
        routes: [
          {
            path: '/',
            component: '../layouts/BasicLayout',
            authority: ['admin', 'user'],
            routes: [
              {
                path: '/',
                redirect: '/welcome',
              },
              {
                path: '/welcome',
                name: 'welcome',
                icon: 'smile',
                component: './Welcome',
              },
              {
                path: '/admin',
                name: 'admin',
                icon: 'crown',
                component: './Admin',
                authority: ['admin'],
                routes: [
                  {
                    path: '/admin/sub-page',
                    name: 'sub-page',
                    icon: 'smile',
                    component: './Welcome',
                    authority: ['admin'],
                  },
                ],
              },
                {
    path: '/antd/user',
    name: '用户管理',
    routes:[
    {
    name: '权限',
    path: '/antd/user/permission/',
    routes: [
        // 增
        {
            name: '新增权限',
            path: '/antd/user/permission/create',

            hideInMenu:true,
        },
        // 改
        {
            name: '权限权限',
            path: '/antd/user/permission/update',

            hideInMenu:true,
        },
        // 查
        {
            name: '权限详情',
            path: '/antd/user/permission/detail',

            hideInMenu:true,
        },
        // 列表
        {
            name: '权限列表',
            path: '/antd/user/permission/list',

        },
    ]
},
    {
    name: 'role-permission relationship',
    path: '/antd/user/role_permissions/',
    routes: [
        // 增
        {
            name: '新增role-permission relationship',
            path: '/antd/user/role_permissions/create',

            hideInMenu:true,
        },
        // 改
        {
            name: '权限role-permission relationship',
            path: '/antd/user/role_permissions/update',

            hideInMenu:true,
        },
        // 查
        {
            name: 'role-permission relationship详情',
            path: '/antd/user/role_permissions/detail',

            hideInMenu:true,
        },
        // 列表
        {
            name: 'role-permission relationship列表',
            path: '/antd/user/role_permissions/list',

        },
    ]
},
    {
    name: '角色',
    path: '/antd/user/role/',
    routes: [
        // 增
        {
            name: '新增角色',
            path: '/antd/user/role/create',

            hideInMenu:true,
        },
        // 改
        {
            name: '权限角色',
            path: '/antd/user/role/update',

            hideInMenu:true,
        },
        // 查
        {
            name: '角色详情',
            path: '/antd/user/role/detail',

            hideInMenu:true,
        },
        // 列表
        {
            name: '角色列表',
            path: '/antd/user/role/list',

        },
    ]
},
    {
    name: 'user-role relationship',
    path: '/antd/user/user_roles/',
    routes: [
        // 增
        {
            name: '新增user-role relationship',
            path: '/antd/user/user_roles/create',

            hideInMenu:true,
        },
        // 改
        {
            name: '权限user-role relationship',
            path: '/antd/user/user_roles/update',

            hideInMenu:true,
        },
        // 查
        {
            name: 'user-role relationship详情',
            path: '/antd/user/user_roles/detail',

            hideInMenu:true,
        },
        // 列表
        {
            name: 'user-role relationship列表',
            path: '/antd/user/user_roles/list',

        },
    ]
},
    {
    name: '用户列表',
    path: '/antd/user/user/',
    routes: [
        // 增
        {
            name: '新增用户列表',
            path: '/antd/user/user/create',

            hideInMenu:true,
        },
        // 改
        {
            name: '权限用户列表',
            path: '/antd/user/user/update',

            hideInMenu:true,
        },
        // 查
        {
            name: '用户列表详情',
            path: '/antd/user/user/detail',

            hideInMenu:true,
        },
        // 列表
        {
            name: '用户列表列表',
            path: '/antd/user/user/list',

        },
    ]
},
    {
    name: 'group-user relationship',
    path: '/antd/user/group_users/',
    routes: [
        // 增
        {
            name: '新增group-user relationship',
            path: '/antd/user/group_users/create',

            hideInMenu:true,
        },
        // 改
        {
            name: '权限group-user relationship',
            path: '/antd/user/group_users/update',

            hideInMenu:true,
        },
        // 查
        {
            name: 'group-user relationship详情',
            path: '/antd/user/group_users/detail',

            hideInMenu:true,
        },
        // 列表
        {
            name: 'group-user relationship列表',
            path: '/antd/user/group_users/list',

        },
    ]
},
    {
    name: 'group-permission relationship',
    path: '/antd/user/group_permissions/',
    routes: [
        // 增
        {
            name: '新增group-permission relationship',
            path: '/antd/user/group_permissions/create',

            hideInMenu:true,
        },
        // 改
        {
            name: '权限group-permission relationship',
            path: '/antd/user/group_permissions/update',

            hideInMenu:true,
        },
        // 查
        {
            name: 'group-permission relationship详情',
            path: '/antd/user/group_permissions/detail',

            hideInMenu:true,
        },
        // 列表
        {
            name: 'group-permission relationship列表',
            path: '/antd/user/group_permissions/list',

        },
    ]
},
    {
    name: '组',
    path: '/antd/user/group/',
    routes: [
        // 增
        {
            name: '新增组',
            path: '/antd/user/group/create',

            hideInMenu:true,
        },
        // 改
        {
            name: '权限组',
            path: '/antd/user/group/update',

            hideInMenu:true,
        },
        // 查
        {
            name: '组详情',
            path: '/antd/user/group/detail',

            hideInMenu:true,
        },
        // 列表
        {
            name: '组列表',
            path: '/antd/user/group/list',

        },
    ]
},
    ]
},
                {
    path: '/antd/order',
    name: '订单管理',
    routes:[
    {
    name: '订单',
    path: '/antd/order/order/',
    routes: [
        // 增
        {
            name: '新增订单',
            path: '/antd/order/order/create',

            hideInMenu:true,
        },
        // 改
        {
            name: '权限订单',
            path: '/antd/order/order/update',

            hideInMenu:true,
        },
        // 查
        {
            name: '订单详情',
            path: '/antd/order/order/detail',

            hideInMenu:true,
        },
        // 列表
        {
            name: '订单列表',
            path: '/antd/order/order/list',

        },
    ]
},
    ]
},
                {
                name: 'list.table-list',
                icon: 'table',
                path: '/list',
                component: './TableList',
              },
              {
                component: './404',
              },
            ],
          },
          {
            component: './404',
          },
        ],
      },
    ],
  },
  {
    component: './404',
  },
];