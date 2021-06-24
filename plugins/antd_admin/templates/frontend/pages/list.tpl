import React from 'react';
import {PageContainer} from '@ant-design/pro-layout';
import type {TableListItem} from './data'
import {Button, Popconfirm, message} from 'antd';
import {query{[ model.name | capitalize ]}, delete{[ model.name | capitalize ]}} from './service'
import {Table, Tag, Space} from 'antd';
import ProTable from '@ant-design/pro-table';
import {history} from 'umi';
import { PlusOutlined } from '@ant-design/icons';


class TableList extends React.Component {

handelDetail(record) {
    history.push({
      pathname: '/antd/{[ app_name ]}/{[ model.name ]}/detail',
      query: {
        id: record.id,
      },
    });
  }

  handelUpdate(record) {
      history.push({
      pathname: '/antd/{[ app_name ]}/{[ model.name ]}/update',
      query: {
        id: record.id,
      },
    });
  }

  handelDelete(record) {
    delete{[ model.name | capitalize ]}(record.id).then(resp=>{
        message.success('删除成功');
            this.setState({
                dataSource: [],
            });
            this.getList()
    })
  }

columns = [
  {% for field in model.fields.values() %}
    {% if field.choices %}
    {
        title: '{[ field.label ]}',
        dataIndex: '{[ field.name ]}',
        key: '{[ field.name ]}',
        valueType: 'radio',
        valueEnum:()=>{
            const valueEnum = {
            {% for choice in field.choices %}
            {[ choice.value ]}:{ status:'{[ choice.value ]}', text:'{[ choice.label ]}' },
            {% endfor %}
            }
            return valueEnum
        }
    },
    {% elif field.type == 'ManyToManyField' %}
    {
        title: '{[ field.label ]}',
        dataIndex: '{[ field.name ]}',
        key: '{[ field.name ]}',
        valueType: 'text',
        render:(elements)=>{
            return elements.join('、')
        }
    },
    {% else %}
    {
        title: '{[ field.label ]}',
        dataIndex: '{[ field.name ]}',
        key: '{[ field.name ]}',
        valueType: '{[ field.type | django_to_protable ]}',
    },
    {% endif %}
    {% endfor %}
  {
    title: '操作',
    key: 'action',
    render: (text, record) => (
      <Space size="middle">
          <Button size='small' type="primary" onClick={() => {
            this.handelDetail(record)
          }}>查看</Button>
          <Button size='small' type="primary" onClick={() => {
            this.handelUpdate(record)
          }}>编辑</Button>
          <Popconfirm
    title="确定要删除这条记录吗?"
    onConfirm={()=>{this.handelDelete(record)}}
    okText="确定"
    cancelText="取消"
  >
    <Button size='small' danger onClick={() => {

          }}>删除</Button>
  </Popconfirm>

        </Space>
    ),
  },
];

  constructor(props) {
    super(props);
    this.state = {
      dataSource: []
    }
  }

  componentDidMount() {
    this.getList()
  }

  getList() {
    query{[ model.name | capitalize ]}().then(res => {
      this.setState({
        dataSource: res.elements,
      });
    })
  }

  render() {
    return (
      <PageContainer>
        <ProTable
        columns={this.columns}
        dataSource={this.state.dataSource}
        toolBarRender={() => [
            <Button
              type="primary"
              key="primary"
              onClick={() => {
                history.push({
                  pathname: '/antd/{[ app_name ]}/{[ model.name ]}/create',
                });
              }}
            >
              <PlusOutlined/> 新建
            </Button>,
          ]}
        />
      </PageContainer>
    )
  }
}

export default TableList;
