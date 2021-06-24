import request from '@/utils/request';
import type { TableListParams, TableListItem } from './data.d';

// {[ model.label ]}查询
export async function query{[ model.name | capitalize ]}(params?: TableListParams) {
  return request('/api/backend/{[ app_name ]}/{[ model.name ]}/', {
    method: 'GET',
    params,
  });
}

// {[ model.label ]}创建
export async function create{[ model.name | capitalize ]}(data) {
  return request('/api/backend/{[ app_name ]}/{[ model.name ]}/', {
    method: 'POST',
    data,
  });
}

// {[ model.label ]}详情
export async function detail{[ model.name | capitalize ]}(pk) {
  return request(`/api/backend/{[ app_name ]}/{[ model.name ]}/${pk}/`, {
    method: 'GET',
  });
}

// {[ model.label ]}更新
export async function update{[ model.name | capitalize ]}(pk, data) {
  return request(`/api/backend/{[ app_name ]}/{[ model.name ]}/${pk}/`, {
    method: 'PUT',
    data,
  });
}

