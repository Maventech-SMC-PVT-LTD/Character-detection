import React, { Component } from 'react';
import { Upload, Icon, Spin } from 'antd'
import axios from 'axios'

class ImageFrom extends Component {
    constructor(props) {
        super(props);
        this.state = {
            imageUrl: "",
            successResponse: false,
            charaterDetect: "",
            responseSent: false,
        }
    }

    handleChange = (data) => {
        console.log("This is image data", data);
    }

    customRequest = (data) => {
        console.log('From react component====', data.file);
        let reader = new FileReader();
        reader.onload = (e) => {
            this.setState({ imageUrl: e.target.result });
        };
        reader.readAsDataURL(data.file);
        var formData = new FormData();
        formData.append("file", data.file);
        this.setState({ responseSent: true, successResponse: false })
        axios.post('/uploadFile', formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        }).then(({ data }) => {
            console.log("this is data ====", data);
            this.setState({ charaterDetect: data.name, successResponse: true })
        })

    }
    render() {
        const { successResponse, charaterDetect, responseSent } = this.state;
        const uploadButton = (
            <div>
                <Icon type={this.state.loading ? 'loading' : 'plus'} style={{ fontSize: 80, width: "500px" }} />
                <div className="ant-upload-text">Upload</div>
            </div>
        );
        const { imageUrl } = this.state;
        return (
            <div>
                <div className="design">
                    <h1>Charater detection (image recognization)</h1>
                    <h2>using (KNN) k-nearest neighbors algorithm</h2>
                    <h3>Note </h3>
                    <p>Please open the file of your character Our sytem will detect that specific character using KNN algorithm</p>
                    <p>And predect the result using artificial intelligance It will help in your childern learning process</p>
                    <p>Hope you will enjoy....... </p>
                    <a href="https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm">Click here for more information</a>
                </div>
                <div className="openimg">
                    <Upload
                        className="uploadDiv"
                        style={{ height: 400, width: 500 }}
                        name="avatar"
                        listType="picture-card"
                        showUploadList={false}
                        action="http://localhost:8080"
                        customRequest={this.customRequest}
                        onChange={this.handleChange}
                    >
                        {imageUrl ? <img src={imageUrl} alt="avatar" style={{ width: '500px' }} /> : uploadButton}
                    </Upload>
                </div>
                {responseSent
                    &&
                    <div>
                        {
                            successResponse
                                ?
                                <div className="resultDiv" >
                                    Our predicted image is: {charaterDetect}
                                </div>
                                : <div className="resultDiv">
                                    <Spin size="large" />
                                </div>
                        }
                    </div>

                }
                <div className="design1">
                    <center>
                        <h2>Copyright all rights reserved CMT Softwares Solution 2019-3019</h2>
                        <h4>Tayyab,najam,adnan & fazeel</h4>
                    </center>

                </div>
            </div>
        );
    }
}

export default ImageFrom;
