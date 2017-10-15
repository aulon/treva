/*
 * © 2017 Tal Globus. All Rights Reserved.
 */

/*
 * © 2017 Tal Globus. All Rights Reserved.
 */

import styles from './styles';
import React, { Component } from 'react';
import { View, Text, Picker, StyleSheet } from 'react-native';

import data from './data';

class PeoplePicker extends Component {
	constructor(props) {
		super(props);
		this.state = {
			num: "1"
		};

		this.updateNumber = (num) => {
			this.setState({ num: num });

		};
	}

	componentWillMount() {
		let max = this.props.max || 8;
		let suffix = this.props.suffix || "";
		this.setState({ range: Array.from(Array(max).keys()).map(elem => ({
			label: elem+1+suffix,
			num: elem+1
		}))});
	}

	render() {
		return (
			<View>
				<Picker style={styles.Picker} itemStyle={styles.item} mode="dropdown" selectedValue = {this.state.num}
						onValueChange = {this.updateNumber}>
					{this.state.range.map(({label, num}) =>
						// <th key={title}>{title}</th>
						<Picker.Item label={label} value={num}
									 key={num} />
					)}
				</Picker>
				{/*<Text style = {styles.text}>{this.state.num}</Text>*/}
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

export default PeoplePicker;