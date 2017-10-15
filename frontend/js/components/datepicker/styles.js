/*
 * © 2017 Tal Globus. All Rights Reserved.
 */

const React = require("react-native");

const { StyleSheet } = React;

let styles = StyleSheet.create({
	dateTouch: {
		width: 142
	},
	dateTouchBody: {
		flexDirection: 'row',
		height: 40,
		alignItems: 'center',
		justifyContent: 'center'
	},
	dateIcon: {
		width: 32,
		height: 32,
		marginLeft: 5,
		marginRight: 5
	},
	dateInput: {
		flex: 1,
		height: 40,
		borderWidth: 1,
		borderColor: '#aaa',
		alignItems: 'center',
		justifyContent: 'center'
	},
	dateText: {
		color: '#333'
	},
	placeholderText: {
		color: '#c9c9c9'
	},
	datePickerMask: {
		flex: 1,
		alignItems: 'flex-end',
		flexDirection: 'row',
		backgroundColor: '#00000077'
	},
	datePickerCon: {
		backgroundColor: '#fff',
		height: 0,
		overflow: 'hidden'
	},
	btnText: {
		position: 'absolute',
		top: 0,
		// height: 22,
		// padding: 10,
		flexDirection: 'row',
		alignItems: 'center',
		justifyContent: 'center'
	},
	btnTextText: {
		fontSize: 16,
		color: '#580095'
	},
	btnTextCancel: {
		color: '#666'
	},
	btnCancel: {
		left: 0
	},
	btnConfirm: {
		right: 0
	},
	datePicker: {
		marginTop: 12,
		borderTopColor: '#ccc',
		borderTopWidth: 0,
		width: 300,
		borderColor: '#aaa',
		borderRadius: 25
	},
	disabled: {
		backgroundColor: '#eee'
	}
});

export default styles;