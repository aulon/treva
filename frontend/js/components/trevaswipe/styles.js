/*
 * © 2017 Tal Globus. All Rights Reserved.
 */

const React = require("react-native");

const { StyleSheet, Dimensions, Platform } = React;

const deviceHeight = Dimensions.get("window").height;

export default {
	imageContainer: {
		flex: 1,
		width: null,
		height: null
	},
	logoContainer: {
		flex: 1,
		marginTop: deviceHeight / 8,
		marginBottom: 30
	},
	logo: {
		position: "absolute",
		left: Platform.OS === "android" ? 40 : 50,
		top: Platform.OS === "android" ? 35 : 60,
		width: 280,
		height: 100
	},
	text: {
		color: "#D8D8D8",
		bottom: 6,
		marginTop: 5
	},
	mb10: {
		marginBottom: 10
	},

	container: {
		backgroundColor: "#FFF"
	},
	buttonContainer: {
		flexDirection: "row",
		flexWrap: "wrap",
		flex: 1,
		justifyContent: "center",
		marginTop: 10
	},
	mb15: {
		marginBottom: 20
	},
	mt15: {
		// marginTop: 15,
		// width: "80%"
	},
	mb20: {
		marginBottom: 20
	},
	iconButton: {
		color: "#007aff"
	},
	margin: {
		flex: 1,
		alignItems: "center",
		justifyContent: "center",
		borderColor: "#FFF"
	},
	mf: {
		flexGrow: 1,
		alignSelf: "center",
		alignItems: "center"
	}
};
