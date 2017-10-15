/*
 * © 2017 Tal Globus. All Rights Reserved.
 */

import React, { Component } from "react";
import { Image, View, StatusBar } from "react-native";

import { Container, Button, H3, Text, Header, Icon, Item, Input, IconNB, Title, Body, Content, Left, Right } from "native-base";

import styles from "./styles";
import MyDatePicker from "../datepicker";
import MyPicker from "../numberpicker";
import Swipe from "../swipe";
import AirportPicker from "../airportpicker/index";

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
				{/*<Image source={launchscreenBg} style={styles.imageContainer}>*/}
					{/*<View style={styles.logoContainer}>*/}
						{/*<Image source={launchscreenLogo} style={styles.logo} />*/}
					{/*</View>*/}
					<View
						style={{
							alignItems: "center",
							marginBottom: 50,
							backgroundColor: "#F2E1FE",
							height: "100%"
						}}
					>
						<Content padder style={{ paddingTop: 20, height: 180 }}>
							{/*<Content padder>*/}
								<Text style={{paddingTop: 10, borderBottomWidth: 0, alignSelf: 'center'}}>Pick Your Point of Origin</Text>
								<AirportPicker/>
								{/*<Item disabled>*/}
									{/*<Input disabled placeholder="Barcelona-El Prat Airport, Barcelona, ES" />*/}
									{/*/!*<IconNB name="ios-information-circle" />*!/*/}
								{/*</Item>*/}
							{/*</Content>*/}
							<Content padder>
								{/*<Text style={{paddingTop: 10, borderBottomWidth: 0}}>Start Date</Text><MyDatePicker />*/}
								{/*<Text style={{paddingTop: 10, borderBottomWidth: 0}}>End Date</Text><MyDatePicker />*/}
								{/*<Text style={{paddingTop: 10, borderBottomWidth: 0}}>Number of People</Text>*/}
								{/*<Text style={{paddingTop: 10, borderBottomWidth: 0}}>Number of People</Text>*/}
								{/*<Text style={{paddingTop: 10, borderBottomWidth: 0}}>Number of People</Text>*/}
								{/*<Text style={{paddingTop: 10, borderBottomWidth: 0}}>Number of People</Text>*/}
								<Text style={{paddingTop: 10, borderBottomWidth: 0}}>Number of People</Text><MyPicker />
								<Text style={{paddingTop: 10, borderBottomWidth: 0}}>End Date</Text><MyDatePicker />
							</Content>
						</Content>
						{/*<H3 style={styles.text}>The World</H3>*/}
						{/*<View style={{ marginTop: 8 }} />*/}
						{/*<H3 style={styles.text}>at the swipe of a finger</H3>*/}
						{/*<View style={{ marginTop: 8 }} />*/}
						<Content padder style={{ paddingTop: 10 }}>
							{/*<Button block info style={styles.mb15}><Text>Info</Text></Button>*/}
							<Button block primary style={styles.mb15}
									onPress={() => this.props.navigation.navigate("Loading")}>
									{/*style={{ backgroundColor: "#c58bc5", alignSelf: "center" }}*/}
									{/*onPress={() => this.props.navigation.navigate("Start")}*/}
								<Text>Trevaswipe</Text>
							</Button>
							{/*<Button block success style={styles.mb15}>*/}
								{/*<Text>Success</Text>*/}
							{/*</Button>*/}
							{/*<Button block dark style={styles.mb15}><Text>Dark</Text></Button>*/}
						</Content>
					</View>
				{/*</Image>*/}
			</Container>
		);
	}
}

export default Start;
