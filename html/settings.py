from app.settings import load


def get_config_html():
    config = load()
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script src="https://unpkg.com/vue@next"></script>
    <link rel="stylesheet" href="https://unpkg.com/element-plus/dist/index.css" />
    <script src="https://unpkg.com/element-plus"></script>
</head>
<body>
<div id="app">
    <el-card class="box-card">
        <template #header>
            <div class="card-header">
                <span>设置</span>
            </div>
        </template>
        <el-form
                ref="formRef"
                :model="form"
                label-width="120px"
                class="demo-dynamic"
        >
            <el-form-item prop="http_proxy" label="http_proxy">
                <el-input v-model="form.http_proxy" />
            </el-form-item>
            <el-form-item prop="https_proxy" label="https_proxy">
                <el-input v-model="form.https_proxy" />
            </el-form-item>
            <el-form-item prop="bing_ua" label="bing_ua">
                <el-input v-model="form.bing_ua" />
            </el-form-item>
            <el-form-item prop="gpt_ua" label="gpt_ua">
                <el-input v-model="form.gpt_ua" />
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="submitForm(formRef)"
                >保存</el-button
                >
                <el-button @click="resetForm(formRef)">重置</el-button>
            </el-form-item>
        </el-form>
    </el-card>
</div>


<script>
    const { createApp, reactive, toRefs, ref } = Vue;
    const vue3Composition = {
        setup(){
            const formRef = ref();
            const form = reactive({
                http_proxy: "%s",
                https_proxy: "%s",
                bing_ua: "%s",
                gpt_ua: "%s",
            });

            const submitForm = (formEl) => {
                if (!formEl) return;
                formEl.validate((valid) => {
                    if (valid) {
                        window.pywebview.api.submit_form(form);
                    } else {
                        console.log("error submit!");
                        return false;
                    }
                });
            };

            const resetForm = (formEl) => {
                if (!formEl) return;
                formEl.resetFields();
            };
            return {
                formRef,
                form,
                submitForm,
                resetForm
            }
        }

    }
    const app = createApp(vue3Composition);
    app.use(ElementPlus);
    app.mount('#app');
</script>
</body>
</html>
    """ % (config.http_proxy, config.https_proxy, config.bing_ua, config.gpt_ua)
