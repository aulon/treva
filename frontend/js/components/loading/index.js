/*
 * © 2017 Tal Globus. All Rights Reserved.
 */

import React, { Component } from "react";

import {
	Container,
	Header,
	Title,
	Content,
	Button,
	Icon,
	Spinner,
	Top,
	Text,
	Left,
	Right,
	Body,
	H2,
	View
} from "native-base";

import styles from "./styles";

class NHSpinner extends Component {
	// eslint-disable-line

	render() {
		return (
			<Container style={styles.container}>
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
					<Title style={{ color: "#FFF" }}>Searching</Title>
					</Body>
					<Right />

				</Header>
				<View
					style={{
						alignItems: "center",
						marginBottom: 50,
						paddingTop: 50,
						backgroundColor: "#F2E1FE",
						height: "100%"
					}}
				>

					<Content>
						<H2 style={{ alignSelf: "center" }}>Finding Your Ideal Getaway...</H2>
						<Content padder style={{ paddingTop: 120}}>
							<Spinner color="blue" />
						</Content>
					</Content>
				</View>
			</Container>
		);
	}
}

export default NHSpinner;
