/*
 * © 2017 Tal Globus. All Rights Reserved.
 */

import styles from './styles';
import React, { Component } from 'react';
import { View, Text, Picker, StyleSheet } from 'react-native';

class NumberPicker extends Component {
	constructor(props) {
		super();
		this.state = {user: ''};

		this.updateUser = (user) => {
			this.setState({ user: user });

		};
	}

	render() {
		return (
			<View>
				<Picker selectedValue = {this.state.user} onValueChange = {this.updateUser}>
					<Picker.Item label = "Steve" value = "steve" />
					<Picker.Item label = "Ellen" value = "ellen" />
					<Picker.Item label = "Maria" value = "maria" />
				</Picker>
				<Text style = {styles.text}>{this.state.user}</Text>
			</View>
		)
	}
}

// const styles = StyleSheet.create({
// 	text: {
// 		fontSize: 30,
// 		alignSelf: 'center',
// 		color: 'red'
// 	}
// });

export default NumberPicker;



// export default class NumberPicker extends Component {
// 	constructor(props){
// 		super(props);
// 		this.state = {language:"java"};
// 	}
//
// 	render(){
// 		return (
// 			<Picker
// 				selectedValue={this.state.language}
// 				onValueChange={(itemValue, itemIndex) => this.setState({language: itemValue})}>
// 				<Picker.Item label="Java" value="java" />
// 				<Picker.Item label="JavaScript" value="js" />
// 			</Picker>
// 		)
// 	}
// }