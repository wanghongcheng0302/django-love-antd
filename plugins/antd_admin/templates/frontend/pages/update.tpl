import { InfoCircleOutlined } from '@ant-design/icons';
import { Button, Card, DatePicker, Input, Form, InputNumber, Radio, Select, Tooltip, message } from 'antd';
import type { Dispatch } from 'umi';
import { connect, FormattedMessage, formatMessage } from 'umi';
import type { FC } from 'react';
import React from 'react';
import { PageContainer } from '@ant-design/pro-layout';
import styles from './style.less';
const FormItem = Form.Item;
const { Option } = Select;
const { RangePicker } = DatePicker;
import {history} from 'umi';
const { TextArea } = Input;
interface BasicFormProps {
  submitting: boolean;
  dispatch: Dispatch;
}

{%- for field in model.fields.values() %}
    {%- if field.type in ["ForeignKey", "ManyToManyField"] %}
        import { query{[ field.to.__name__ | capitalize ]} } from '@/pages/{[ field.to._meta.app_config.name ]}/{[ field.to.__name__.lower() ]}/service.ts'
    {%- endif %}
{%- endfor %}
import { update{[ model.name | capitalize ]}, detail{[ model.name | capitalize ]} } from './service'

const formItemLayout = {
    labelCol: {
      xs: {
        span: 24,
      },
      sm: {
        span: 7,
      },
    },
    wrapperCol: {
      xs: {
        span: 24,
      },
      sm: {
        span: 12,
      },
      md: {
        span: 10,
      },
    },
  };
  const submitFormLayout = {
    wrapperCol: {
      xs: {
        span: 24,
        offset: 0,
      },
      sm: {
        span: 10,
        offset: 7,
      },
    },
  };

class BasicForm extends React.Component<BasicFormProps> {
  constructor(props) {
    super(props);
  this.state = {
    {%- for field in model.fields.values() %}
      {%- if field.type in ["ForeignKey", "ManyToManyField"] %}
          {[ field.name ]}Options: [],
      {% endif %}
    {%- endfor %}
    formData:{id:this.props.location.query.id},
    }
  }

  componentDidMount() {
    {%- for field in model.fields.values() %}
      {%- if field.type in ["ForeignKey", "ManyToManyField"] %}
          query{[ field.to.__name__ | capitalize ]}().then(resp=>{
            this.setState({
                {[ field.name ]}Options: resp.elements
            });
          })
      {% endif %}
    {%- endfor %}
    console.log(this.props.location.query)

    detail{[ model.name | capitalize ]}(this.state.formData.id).then(resp=>{
        if (resp.rc === 200) {
        this.setState({
          formData: resp.fields
        })
      }
      this.refs['form'].setFieldsValue(this.state.formData)
    })
  }

onFinish(values){
    console.log('-----> 表单', values)
    const pk = values.id
    update{[ model.name | capitalize ]}(pk, values).then(resp=>{
        if(resp.rc === 200){
            message.success('更新成功');
            setTimeout(()=>{
              history.push({
              pathname: '/antd/{[ app_name ]}/{[ model.name ]}/list',
              });
            }, 1000)
        }
    })
  }

    render(){
   return (
    <PageContainer content="表单页用于向用户收集或验证信息，基础表单常见于数据项较少的表单场景。">
      <Card bordered={false}>
        <Form ref='form'
          style={{
            marginTop: 8,
          }}
                  onFinish={(values)=>{this.onFinish({...this.state.formData, ...values})}}
              ref='form'
        >
        {%- for field in model.fields.values() %}
            {%- if field.auto_now or field.auto_now_add or field.auto_created or field.is_primary_key %}
                {% continue %}
            {%- endif %}
        {%- if field.choices -%}
        <FormItem
            {...formItemLayout}
            label={"{[ field.label ]}"}
            name="{[ field.name ]}"
            rules={ [{
            {%- if not field.blank -%}
                required: true,
            {%- endif -%}
                type: "{[ field.type | django_convert_typescript ]}",
            {%- if field.max_length -%}
                max: {[ field.max_length ]}
            {%- endif -%}}] }
            >
            <Radio.Group>
            {%- for choice in field.choices %}
                <Radio value={ {[ choice.value ]} }>{[ choice.label ]}</Radio>
            {%- endfor %}
            </Radio.Group>
          </FormItem>
        {%- elif field.type in ['CharField', 'EmailField'] -%}
        <FormItem
            {...formItemLayout}
            label={"{[ field.label ]}"}
            name="{[ field.name ]}"
            rules={ [{
            {%- if not field.blank -%}
                required: true,
            {%- endif -%}
                type: "{[ field.type | django_convert_typescript ]}",
            {%- if field.max_length -%}
                max: {[ field.max_length ]}
            {%- endif -%}}] }
            >
            <Input placeholder="请输入{[ field.label ]}" />
          </FormItem>
        {%- elif field.type in ['BigAutoField', 'BigIntegerField', 'DecimalField', 'FloatField', 'IntegerField', 'PositiveBigIntegerField', 'PositiveIntegerField', 'PositiveSmallIntegerField', 'SmallIntegerField'] -%}
         <FormItem
            {...formItemLayout}
            label={"{[ field.label ]}"}
            name="{[ field.name ]}"
            rules={ [{
            {%- if not field.blank -%}
                required: true,
            {%- endif -%}
                type: "{[ field.type | django_convert_typescript ]}",
            {%- if field.max_length -%}
                max: {[ field.max_length ]}
            {%- endif -%}}] }
            >
            <InputNumber />
          </FormItem>
        {%- elif field.type in ['DateField', 'DateTimeField', 'timefield',] -%}
        <FormItem
            {...formItemLayout}
            label={"{[ field.label ]}"}
            name="{[ field.name ]}"
            rules={ [{
            {%- if not field.blank -%}
                required: true,
            {%- endif -%}
                type: "{[ field.type | django_convert_typescript ]}",
            {%- if field.max_length -%}
                max: {[ field.max_length ]}
            {%- endif -%}}] }
            >
            <DatePicker  />
          </FormItem>
        {%- elif field.type in ['TextField', ] -%}
        <FormItem
            {...formItemLayout}
            label={"{[ field.label ]}"}
            name="{[ field.name ]}"
            rules={ [{
            {%- if not field.blank -%}
                required: true,
            {%- endif -%}
                type: "{[ field.type | django_convert_typescript ]}",
            {%- if field.max_length -%}
                max: {[ field.max_length ]}
            {%- endif -%}}] }
            >
            <TextArea showCount  />
          </FormItem>
        {%- elif field.type in ['ForeignKey', ] -%}
           <FormItem
            {...formItemLayout}
            label={"{[ field.label ]}"}
            name="{[ field.name ]}"
            rules={ [{
            {%- if not field.blank -%}
                required: true,
            {%- endif -%}
                type: "{[ field.type | django_convert_typescript ]}",
            {%- if field.max_length -%}
                max: {[ field.max_length ]}
            {%- endif -%}}] }
            >
            <Select style={{ width: 120 }} >
                {
                    this.state.{[ field.name ]}Options.map(item => {
                        return <Option key={item.id} value={item.id}>{ item.obj_ }</Option>
                    })
                }
            </Select>
          </FormItem>
        {%- elif field.type in ['ManyToManyField', ] %}
            <FormItem
            {...formItemLayout}
            label={"{[ field.label ]}"}
            name="{[ field.name ]}"
          >
            <Select style={{ width: 120 }} mode="multiple" >
                {
                    this.state.{[ field.name ]}Options.map(item => {
                        return <Option key={item.id} value={item.id}>{ item.obj_ }</Option>
                    })
                }
            </Select>
          </FormItem>
        {%- endif %}
        {% endfor %}
          <FormItem
            {...submitFormLayout}
            style={{ marginTop: 32 }}
          >
            <Button type="primary" htmlType="submit" loading={this.submitting}>
              提交
            </Button>
            <Button
              style={{
                marginLeft: 8,
              }}
            >
              保存
            </Button>
          </FormItem>
        </Form>
      </Card>
    </PageContainer>
  );
    }


};

export default connect(
  ({
    loading,
  }: {
    loading: {
      effects: Record<string, boolean>;
    };
  }) => ({
    submitting: loading.effects['formAndbasicForm/submitRegularForm'],
  }),
)(BasicForm);
