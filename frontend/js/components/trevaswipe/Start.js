/*
 * © 2017 Tal Globus. All Rights Reserved.
 */

import React, { Component } from "react";
import { Image, View, StatusBar } from "react-native";

import { Container, Button, H3, Text, Header, Icon, Title, Body, Left, Right } from "native-base";

import styles from "./styles";
import MyDatePicker from "../datepicker";

const launchscreenBg = require("../../../img/launchscreen-bg.png");
const launchscreenLogo = require("../../../img/logo-kitchen-sink.png");

class Start extends Component {
	// eslint-disable-line

	render() {
		return (
			<Container style={styles.container}>
				<StatusBar barStyle="light-content" />
				<Header
					style={{ backgroundColor: "#580095" }}
					androidStatusBarColor="#580095"
					iosBarStyle="light-content"
				>
					<Left>
						<Button transparent onPress={() => this.props.navigation.goBack()}>
							<Icon name="arrow-back" style={{ color: "#FFF" }} />
						</Button>
					</Left>
					<Body>
					<Title style={{ color: "#FFF" }}>Get Started</Title>
					</Body>
					<Right />

				</Header>
				<Image source={launchscreenBg} style={styles.imageContainer}>
					<View style={styles.logoContainer}>
						<Image source={launchscreenLogo} style={styles.logo} />
					</View>
					<View
						style={{
							alignItems: "center",
							marginBottom: 50,
							backgroundColor: "transparent",
						}}
					>
						<MyDatePicker />
						{/*<H3 style={styles.text}>The World</H3>*/}
						{/*<View style={{ marginTop: 8 }} />*/}
						{/*<H3 style={styles.text}>at the swipe of a finger</H3>*/}
						{/*<View style={{ marginTop: 8 }} />*/}
					</View>
					<View style={{ marginBottom: 80 }}>
						<Button
							style={{ backgroundColor: "#c58bc5", alignSelf: "center" }}
							onPress={() => this.props.navigation.navigate("Start")}
						>
							<Text>Lets Gond!</Text>
						</Button>
					</View>
				</Image>
			</Container>
		);
	}
}

export default Start;
