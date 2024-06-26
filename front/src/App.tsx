import React, { Component } from "react";
import { Route } from "react-router-dom";
import {
  HomePage,
  AboutPage,
  LoginPage,
  DetailPage,
  PerfumePage,
  SurveyPage,
  UserRank,
  SurveyIntroPage,
  SurveyResultPage,
  ExpSurveyPage,
  InfoPage
} from "./pages";
import storage from "lib/storage";
import { connect } from "react-redux";
import { bindActionCreators } from "redux";
import * as userActions from "redux/modules/user";

interface AppProps {
  UserActions: any;
}

class App extends Component<AppProps> {
  initializeUserInfo = async () => {
    const loggedInfo = storage.get("loggedInfo"); // 로그인 정보를 로컬스토리지에서 가져옵니다.
    if (!loggedInfo) return; // 로그인 정보가 없다면 여기서 멈춥니다.

    const { UserActions } = this.props;
    UserActions.setLoggedInfo(loggedInfo);
    try {
      await UserActions.checkStatus();
    } catch (e) {
      storage.remove("loggedInfo");
      window.location.href = "/auth/login?expired";
    }
  };

  componentDidMount() {
    this.initializeUserInfo();
  }

  render() {
    return (
      <div className="App" style={{backgroundColor: '#fbfbfb'}}>
        <Route exact path="/" component={HomePage} />
        <Route exact path="/about" component={AboutPage} />
        <Route path="/perfume/" component={PerfumePage} />
        <Route path="/auth" component={LoginPage} />
        <Route exact path="/detail/:id" component={DetailPage} />
        <Route exact path="/expsurvey" component={ExpSurveyPage} />
        <Route path="/survey" component={SurveyPage} />
        <Route path="/result" component={SurveyResultPage} />
        <Route exact path="/info" component={InfoPage} />
        <Route exact path="/surveyintro" component={SurveyIntroPage} />
        <Route path="/rank" component={UserRank} />
      </div>
    );
  }
}

export default connect(null, (dispatch) => ({
  UserActions: bindActionCreators(userActions, dispatch),
}))(App);
